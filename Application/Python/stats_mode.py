import re
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import os

import plotly.io as pio
pio.renderers.default='browser'

graph_type = [
    "0: Retour au menu précédent",
    "1: Circulaire",
    "2: Histogramme",
    "3: Carte",
    "4: Nuage de points",
    "5: Lignes",
    "6: Zones",
    "7: Soleil"
]

requests_name = [
    "0: Retour au menu précédent",
    "1: Nombre d'établissements par académie",

]

requests_label = [
    "SELECT academie FROM academie ;",

]

requests = [
    "SELECT COUNT(*) AS \"Nombre d\'établissements\", academie.academie AS \"Académie\" FROM Etablissement,academie WHERE Etablissement.academie = academie.academie GROUP BY academie.academie ;"
]

x_label = [
    "Académie",
]

y_label = [
    "Nombre d'établissements",
]

"""
    Fonction de lancement du mode Statistiques
"""
def display_graph(mydb):
    while(True):
        print("Sélectionner le type de graphique:")
        for graph in graph_type:
            print(graph)
        type = input("> ")
        #Quitter le mode
        if type == '0':
            os.system('cls||clear')
            break
        if type == '1':
            circular_graph(mydb)
        if type == '2':
            histogram_graph(mydb)
        if type == '3':
            map_graph(mydb)
        if type == '4':
            cloud_graph(mydb)
        if type == '5':
            line_graph(mydb)
        if type == '6':
            area_graph(mydb)
        if type == '7':
            sunburst_graph(mydb)
        
"""
    Mode graphe circulaire
"""
def circular_graph(mydb):
    while(True):
        print("Sélectionner une requête SQL:")
        for name in requests_name:
            print(name)
        index = input("> ")
        if index == '0':
            os.system('cls||clear')
            break
        else:
            request = requests[int(index)-1]
        #Récupération des noms des colonnes
        label_cursor = mydb.cursor()
        label_cursor.execute(requests_label[int(index)-1])
        label_data = label_cursor.fetchall()
        labels = []
        for x in label_data:
            labels.append(''.join(re.findall(r'[A-Za-z]', str(x))))

        #Récupération des données
        values_cursor = mydb.cursor()
        values_cursor.execute(request)
        values_data = values_cursor.fetchall()
        values = []
        for x in values_data:
            values.append(''.join(re.findall(r'\d', str(x))))

        #Affichage du graphe dans le navigateur (127.0.0.1)
        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig.show()

def histogram_graph(mydb):
    while(True):
        print("Sélectionner une requête SQL:")
        for name in requests_name:
            print(name)
        index = input("> ")
        if index == '0':
            os.system('cls||clear')
            break
        else:
            request = requests[int(index)-1]
        #Récupération des noms des colonnes
        label_cursor = mydb.cursor()
        label_cursor.execute(requests_label[int(index)-1])
        label_data = label_cursor.fetchall()
        labels = []
        for x in label_data:
            labels.append(''.join(re.findall(r'[A-Za-z]', str(x))))

        #Récupération des données
        values_cursor = mydb.cursor()
        values_cursor.execute(request)
        values_data = values_cursor.fetchall()
        values = []
        for x in values_data:
            values.append(''.join(re.findall(r'\d', str(x))))

        df = pd.read_sql_query(request,mydb)
        # Here we use a column with categorical data
        fig = px.histogram(df, x=x_label[int(index)-1], y=y_label[int(index)-1])
        fig.show()

def map_graph(mydb):
    while(True):
        print("Sélectionner une requête SQL:")
        for name in requests_name:
            print(name)
        index = input("> ")
        if index == '0':
            os.system('cls||clear')
            break
        else:
            request = requests[int(index)-1]
        df = pd.read_sql_query(request,mydb)
        geojson = px.data.election_geojson()

        fig = px.choropleth_mapbox(df, geojson=geojson, color="Nombre d'établissements",
                                featureidkey="properties.district",
                                center={"lat": 45.5517, "lon": -73.7073},
                                mapbox_style="carto-positron", zoom=9)
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.show()

def cloud_graph(mydb):
    while(True):
        print("Sélectionner une requête SQL:")
        for name in requests_name:
            print(name)
        index = input("> ")
        if index == '0':
            os.system('cls||clear')
            break
        else:
            request = requests[int(index)-1]
        df = pd.read_sql_query(request,mydb)
        fig = px.scatter_matrix(df)
        fig.show()

def line_graph(mydb):
    while(True):
        print("Sélectionner une requête SQL:")
        for name in requests_name:
            print(name)
        index = input("> ")
        if index == '0':
            os.system('cls||clear')
            break
        else:
            request = requests[int(index)-1]
        df = pd.read_sql_query(request,mydb)
        fig = px.line(df, x=x_label[int(index)-1], y=y_label[int(index)-1], title=requests_name[int(index)-1])
        fig.show()

def area_graph(mydb):
    while(True):
        print("Sélectionner une requête SQL:")
        for name in requests_name:
            print(name)
        index = input("> ")
        if index == '0':
            os.system('cls||clear')
            break
        else:
            request = requests[int(index)-1]
        df = pd.read_sql_query(request,mydb)
        fig = px.area(df, x=x_label[int(index)-1], y=y_label[int(index)-1], color=x_label[int(index)-1], line_group=y_label[int(index)-1])
        fig.show()

"""
    - Université géré par une autre
    - Organisme sous tutelle
"""
def sunburst_graph(mydb):
    while(True):
        print("Sélectionner une requête SQL:")
        for name in requests_name:
            print(name)
        index = input("> ")
        if index == '0':
            os.system('cls||clear')
            break
        else:
            request = requests[int(index)-1]
    #Récupération des noms des colonnes
    label_cursor = mydb.cursor()
    label_cursor.execute(requests_label[int(index)-1])
    label_data = label_cursor.fetchall()
    labels = []
    for x in label_data:
        labels.append(''.join(re.findall(r'[A-Za-z]', str(x))))

    #Récupération des données
    values_cursor = mydb.cursor()
    values_cursor.execute(request)
    values_data = values_cursor.fetchall()
    values = []
    for x in values_data:
        values.append(''.join(re.findall(r'\d', str(x))))

    df = px.data.tips()
    fig = px.sunburst(df, path=['day', 'time', 'sex'], values='total_bill')
    fig.show()