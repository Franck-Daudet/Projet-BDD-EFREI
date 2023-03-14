import mysql.connector
import plotly.express as px
from display_data import display_data
import os


def requests():
    mydb=mysql.connector.connect(
        host="143.42.63.50",
        user="ines",
        passwd="mbap",
        database="Main"
        )
    requests_label = [
        "0: Retour au menu précédent",
        "1: Etablissements hors de Paris",
        "2: Etablissements sous tutelle du Ministère de l'Education Nationale et de la Jeunesse",
        "3: Téléphone qui commencent par 07",
        "4: Nom des établissements et leurs communes",
        "5: Tous les départements des établissements",
        "6: Nom et commune des établissements qui appartiennent à l'académie de Créteil",
        "999: Taper sa propre requête"
    ]
    requests = [
        "select * from Etablissement where lower(commune) <>'paris';",
        "SELECT * FROM Etablissement WHERE id_tutelle = (SELECT id FROM organisme_tutelle where lower(nom_organisme) = \"ministère chargé de l'éducation nationale et de la jeunesse\");",
        "SELECT nom,téléphone FROM `Etablissement` WHERE téléphone LIKE '07%';",
        "SELECT nom, commune FROM `Etablissement`;",
        "SELECT département FROM `Etablissement`;",
        "SELECT nom,commune From `Etablissement`WHERE academie ='Créteil';"
        ]
    while(True):
        print("Sélectionner une requête SQL:")
        for label in requests_label:
            print(label)
        index = input("> ")
        if index == '0':
            os.system('cls||clear')
            break
        if index == '999':
            request = input("Taper votre requête SQL:\n> ")
        else:
            request = requests[int(index)-1]
        myc = mydb.cursor()
        myc.execute(request)
        myres = myc.fetchall()
        display_data(myc,myres)
        