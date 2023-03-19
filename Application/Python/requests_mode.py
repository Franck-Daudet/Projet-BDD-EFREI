import os
from tabulate import tabulate
import csv
import mysql.connector

requests_name = [
    "0: Retour au menu précédent",
    "1: Etablissements hors de Paris",
    "2: Etablissements sous tutelle du Ministère de l'Education Nationale et de la Jeunesse et ayant le label 'Génération 2024'",
    "3: Etablissements dont le contact est un numéro mobile",
    "4: Nom et commune des établissements qui appartiennent à l'académie de Créteil",
    "5: Nombre d'établissements par académie",
    "6: Ensemble des lycées",
    "7: Etablissements et leurs départements",
    "8: Etablissements avec formations spécialisées et leurs taux d'insertion",
    "9: Etablissements privés et leur taux d'insertion et de poursuites d'étude",
    "10: Nombre d'établissements liés pour chaque établissement",
    "11: Nombre d'établissements sous tutelle du Ministère de l\'Agriculture et de la Souveraineté alimentaire par région",
    "12: Les CFA publics et leurs statistiques",
    "13: CFA avec un taux de poursuite d'études supérieur à 50%",
    "14: CFA avec un taux de contrats interrompus supérieur à 50%",
    "15: Etablissements privés avec un taux d'emploi à 12 mois supérieur à 80%",
    "999: Afficher les tables"
    ]

requests_body = [
    "select nom,commune from Etablissement where lower(commune) <>'paris';",
    "SELECT Nom, commune FROM Etablissement WHERE lower(tutelle) = lower(\"ministère chargé de l\'éducation nationale et de la jeunesse\") AND labelGeneration2024 = 1;",
    "SELECT nom,téléphone FROM Etablissement WHERE téléphone LIKE('07%') OR téléphone LIKE('06%');",
    "SELECT nom,commune From Etablissement WHERE academie = 'Créteil';",
    "SELECT academie, COUNT(*) AS \"Nombre d'établissements\" FROM Etablissement GROUP BY academie;",
    "Select nom, commune from Etablissement where nom like 'Lycée%';",
    "SELECT nom,département FROM `Etablissement`;",
    "SELECT nom, taux_poursuite_etudes FROM Etablissement inner JOIN Inserjeune ON Etablissement.UAI = Inserjeune.uai WHERE type LIKE \"ecole%\";",
    "SELECT Nom, taux_emploi_6_mois, taux_poursuite_etudes FROM Etablissement_avec_stat WHERE statut LIKE 'prive%';",
    "SELECT Nom_etablissement, COUNT(Etablissement_lié.Nom_etablissement_lié) FROM Etablissement_lié GROUP BY Nom_etablissement;",
    "SELECT région ,COUNT(*) FROM Etablissement_superieur WHERE tutelle = \"Ministère de l\'Agriculture et de la Souveraineté alimentaire\" GROUP BY région;",
    "SELECT nom, taux_poursuite_etudes, taux_emploi_6_mois, taux_emploi_6_mois_attendu, taux_emploi_12_mois, taux_contrats_interrompus FROM Etablissement_avec_stat WHERE statut = \"public\" AND type = \"Centre de formation d'apprentis\";",
    "SELECT Nom, taux_poursuite_etudes FROM Etablissement_avec_stat WHERE taux_poursuite_etudes >= 50;",
    "SELECT Nom, taux_contrats_interrompus FROM Etablissement_avec_stat WHERE taux_contrats_interrompus >= 50 ORDER BY taux_contrats_interrompus DESC;",
    "SELECT Etablissement_avec_stat.Nom,taux_emploi_12_mois FROM Etablissement_avec_stat INNER JOIN Etablissement_superieur Es on Etablissement_avec_stat.UAI = Es.UAI WHERE taux_emploi_12_mois >= 80 AND Etablissement_avec_stat.statut LIKE 'prive%';",
]

requests_headers = [
    ["Nom", "Commune"],
    ["Nom", "Commune"],
    ["Nom", "Téléphone"],
    ["Nom", "Commune"],
    ["Académie"],
    ["Nom", "Commune"],
    ["Nom", "Département"],
    ["Nom", "Taux de poursuite d'études"],
    ["Nom", "Taux d'emploi à 6 mois","Taux de poursuite d'études"],
    ["Nom", "Nombre d'établissements liés"],
    ["Région", "Nombre d'établissements"],
    ["Nom", "Taux de poursuite d'études", "Taux d'emploi à 6 mois", "Taux d'emploi à 6 mois attendu", "Taux d'emploi à 12_mois", "Taux de contrats interrompus"],
    ["Nom", "Taux de poursuite d'études"],
    ["Nom", "Taux de contrats interrompus"],
    ["Nom", "Taux d'emploi à 12 mois"]
]

csv_names =  [
    'Etablissements_hors_de_Paris.csv',
    'Etablissements_sous_tutelle_du_Ministère_de_l\'Education_Nationale_et_de_la_Jeunesse_et_ayant_le_label_\'Génération_2024\'.csv',
    'Etablissements_dont_le_contact_est_un_numéro_mobile.csv',
    'Nom_et_commune_des_établissements_qui_appartiennent_à_l\'académie_de_Créteil.csv',
    'Nombre_d\'établissements_par_académie.csv',
    'Ensemble_des_lycées.csv',
    'Etablissements_et_leurs_départements.csv',
    'Etablissements_avec_formations_spécialisées_et_leurs_taux_d\'insertion.csv',
    'Etablissements_privés_et_leur_taux_d\'insertion_et_de_poursuites_d\'étude.csv',
    'Nombre_d\'établissements_liés_pour_chaque_établissement .csv',
    'Nombre_d\'établissements_sous_tutelle_du_Ministère_de_l\'Agriculture_et_de_la_Souveraineté_alimentaire_par_région.csv',
    'Les_CFA_publics_et_leurs_statistiques.csv',
    'CFA_avec_un_taux_de_poursuite_d\'études_supérieur_à_50%.csv',
    'CFA_avec_un_taux_de_contrats_interrompus_supérieur_à_50%.csv',
    'Etablissements_privés_avec_un_taux_d\'emploi_à_12_mois_supérieur_à_80%.csv',
]
"""
    Fonction de lancement du mode requêtes
"""
def requests_mode(mydb):
    while(True):
        print("Sélectionner une requête SQL:")
        for name in requests_name:
            print(name)
        try:
            index = input("> ")
            #Quitter le mode
            if index == '0':
                os.system('cls||clear')
                break
            if index == '999':
                show_tables(mydb)
                print('\n')
                continue
            #Taper sa propre requête
            request = requests_body[int(index)-1]
        except (ValueError, IndexError):
            print("\nSaisissez une valeur valide\n")
            continue
        #Placement du curseur dans la bdd
        myc = mydb.cursor()
        #Execution de la requête
        try:
            myc.execute(request)
        except mysql.connector.errors.ProgrammingError:
            print("\nRequête invalide\n")
            continue
        myres = myc.fetchall()
        try :
            with open(csv_names[int(index)-1], 'w', newline='') as fp:
                writer = csv.writer(fp)
                writer.writerow(requests_headers[int(index)-1])
                for result in myres:
                    writer.writerow(result)
        except KeyboardInterrupt :
            print("\n\n********************** Interruption de l'affichage **********************\n")

def show_tables(mydb):
    myc = mydb.cursor()
    myc.execute("SHOW TABLES")
    table_name = []
    for table in myc:
        table_name += (table[0],)


    for table in table_name :
        myc.execute("Explain "+table)
        print()
        print( "-----------------------------------------------------------------------------------------------------------------------")
        print("TABLE : " + table)
        print ("COLONNES : ", end='')
        for x in myc:
            print (x[0]+ " | ", end='')