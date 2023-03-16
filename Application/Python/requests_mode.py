import os
from tabulate import tabulate

requests_name = [
    "0: Retour au menu précédent",
    "1: Etablissements hors de Paris",
    "2: Etablissements sous tutelle du Ministère de l'Education Nationale et de la Jeunesse",
    "3: Téléphone qui commencent par 07",
    "4: Nom des établissements et leurs communes",
    "5: Tous les départements des établissements",
    "6: Nom et commune des établissements qui appartiennent à l'académie de Créteil",
    "7: Nombre d'établissements par académie",
    "999: Taper sa propre requête"
]
requests_body = [
    "select nom from Etablissement where lower(commune) <>'paris';",
    "SELECT * FROM Etablissement WHERE id_tutelle = (SELECT id FROM organisme_tutelle where lower(nom_organisme) = \"ministère chargé de l'éducation nationale et de la jeunesse\");",
    "SELECT nom,téléphone FROM `Etablissement` WHERE téléphone LIKE '07%';",
    "SELECT nom, commune FROM `Etablissement`;",
    "SELECT département FROM `Etablissement`;",
    "SELECT nom,commune From `Etablissement`WHERE academie ='Créteil';",
    "SELECT academie.academie, COUNT(*) AS \"Nombre d'établissements\" FROM Etablissement,academie WHERE Etablissement.academie = academie.academie GROUP BY academie.academie;"
]
"""
    Fonction de lancement du mode requêtes
"""
def requests_mode(mydb):
    while(True):
        print("Sélectionner une requête SQL:")
        for name in requests_name:
            print(name)
        index = input("> ")
        #Quitter le mode
        if index == '0':
            os.system('cls||clear')
            break
        #Taper sa propre requête
        if index == '999':
            request = input("Taper votre requête SQL:\n> ")
        else:
            request = requests_body[int(index)-1]
        #Placement du curseur dans la bdd
        myc = mydb.cursor()
        #Execution de la requête
        myc.execute(request)
        myres = myc.fetchall()
        try :
            #Affichage du résultat de la requête
            display_data(myc,myres)
        except KeyboardInterrupt :
            print("\n\n********************** Interruption de l'affichage **********************\n")

"""
    Fonction d'affichage du résultat des requêtes
"""
def display_data(cursor,data):
    field_names = [i[0] for i in cursor.description]
    print(tabulate(data, headers=field_names,tablefmt='fancy_grid'))