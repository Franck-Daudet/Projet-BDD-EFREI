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
    "3: Nuage de points",
    "4: Lignes",
    "5: Zones",
]

requests_name = [
    "0: Retour au menu précédent",
    "1: Nombre d'établissements par région",
    "2: Nombre d'établissements par académie",
    "3: Etablissements avec formations spécialisées et leurs taux d'insertion",
    "4: Nombre d'établissements liés à chaque établissement",
    "5: CFA avec un taux de contrats interrompus supérieur à 50%",
    "6: Etablissements privé avec un taux d'emploi à 12 mois supérieur à 80%",
    ]

requests_label = [
    "SELECT région FROM Etablissement;",
    "SELECT academie FROM Etablissement;",
    "SELECT nom FROM Etablissement inner JOIN Inserjeune ON Etablissement.UAI = Inserjeune.uai WHERE type LIKE \"ecole%\";",
    "SELECT DISTINCT  Nom_etablissement FROM Etablissement_lié WHERE Etablissement_lié.Nom_etablissement_lié IS NOT NULL;",
    "SELECT Nom FROM Etablissement_avec_stat WHERE taux_contrats_interrompus >= 50",
    "SELECT Etablissement_avec_stat.Nom FROM Etablissement_avec_stat INNER JOIN Etablissement_superieur Es on Etablissement_avec_stat.UAI = Es.UAI WHERE taux_emploi_12_mois >= 80 AND Etablissement_avec_stat.statut LIKE 'prive%';",


]

requests_body = [
    "Select région, COUNT(*) AS \"Nombre d'établissements\" from Etablissement GROUP BY région;",
    "SELECT academie AS 'Académie', COUNT(*) AS \"Nombre d'établissements\" FROM Etablissement GROUP BY academie;",
    "SELECT nom, taux_poursuite_etudes AS 'Taux de poursuite d'étude' FROM Etablissement inner JOIN Inserjeune ON Etablissement.UAI = Inserjeune.uai WHERE type LIKE \"ecole%\";",
    "SELECT Nom_etablissement AS \"Nom d'établissement\", COUNT(Etablissement_lié.Nom_etablissement_lié) AS \"Nombre d'établissement liés\" FROM Etablissement_lié GROUP BY Nom_etablissement;",
    "SELECT Nom as \"Nom\", taux_contrats_interrompus AS 'Taux de contrats interrompus' FROM Etablissement_avec_stat WHERE taux_contrats_interrompus >= 50 ORDER BY taux_contrats_interrompus DESC;",
    "SELECT Etablissement_avec_stat.Nom AS 'Nom', taux_emploi_12_mois AS \"Taux d'emploi à 12 mois\" FROM Etablissement_avec_stat INNER JOIN Etablissement_superieur Es on Etablissement_avec_stat.UAI = Es.UAI WHERE taux_emploi_12_mois >= 80 AND Etablissement_avec_stat.statut LIKE 'prive%';"
]

x_label = [
    "région",
    "Académie",
    "nom",
    "Nom d'établissement",
    "Nom",
    "Nom"
]

y_label = [
    "Nombre d'établissements",
    "Nombre d'établissements",
    "Taux de poursuite d'étude",
    "Nombre d'établissement liés",
    "Taux de contrats interrompus",
    "Taux d'emploi à 12 mois"
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
            cloud_graph(mydb)
        if type == '4':
            line_graph(mydb)
        if type == '5':
            area_graph(mydb)
        
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
            request = requests_body[int(index)-1]
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
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, title=requests_name[int(index)], textinfo='label+percent', insidetextorientation='radial')])
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
            request = requests_body[int(index)-1]
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
            request = requests_body[int(index)-1]
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
            request = requests_body[int(index)-1]
        df = pd.read_sql_query(request,mydb)
        fig = px.line(df, x=x_label[int(index)-1], y=y_label[int(index)-1], title=requests_name[int(index)])
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
            request = requests_body[int(index)-1]
        df = pd.read_sql_query(request,mydb)
        fig = px.area(df, x=x_label[int(index)-1], y=y_label[int(index)-1], color=x_label[int(index)-1], line_group=y_label[int(index)-1])
        fig.show()