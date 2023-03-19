import mysql.connector
from requests_mode import requests_mode
from stats_mode import display_graph
from art import tprint
import os

"""
    Connexion à la base de données
"""
mydb=mysql.connector.connect(
    host="XXX.XXX.XXX.XXX",
    user="XXXX",
    passwd="XXXX",
    database="XXXX"
    )

welcome = tprint("Insertion Stats",chr_ignore=True)
print("Bienvenue sur Insertion Stats\n")
while(True):
    print("Sélectionnner un mode:\n")
    print("0: Stopper l'application\n1: Requêtes SQL\n2: Statistiques")
    mode = input("> ")
    
    #Fermer l'application
    if mode == '0':
        mydb.close()
        exit()
    #Lancer le mode Requêtes SQL
    if mode == '1':
        os.system('cls||clear')
        requests_mode(mydb)
    #Lancer le mode Statistiques
    if mode == '2' :
        os.system('cls||clear')
        display_graph(mydb)