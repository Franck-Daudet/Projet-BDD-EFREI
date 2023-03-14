import mysql.connector
import plotly.express as px
from requests import requests
import os

mydb=mysql.connector.connect(
    host="143.42.63.50",
    user="temp",
    passwd="temp",
    database="Main"
    )
print("Bienvenue sur nom_projet")
while(True):
    print("Sélectionnner un mode:\n")
    print("1: Requêtes SQL\n2: Statistiques\n0: Stopper l'application")
    mode = input("> ")
    if mode == '1':
        os.system('cls||clear')
        requests()
    # if mode == 2 :
    if mode == '0':
        exit()