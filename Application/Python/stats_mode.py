import re
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import os

import plotly.io as pio
pio.renderers.default='browser'

graph_type = [
    "0: Retour au menu précédent",
    "1: Graphique circulaire"
]

requests_name = [
    "0: Retour au menu précédent",
    "1: Nombre d'établissements par académie"
]

requests_label = [
    "SELECT academie FROM academie ;"
]

requests = [
    "SELECT COUNT(*) AS \"Nombre d\'établissements\" FROM Etablissement,academie WHERE Etablissement.academie = academie.academie GROUP BY academie.academie ;"
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