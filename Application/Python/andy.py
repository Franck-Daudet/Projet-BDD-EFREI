import mysql.connector
import plotly.express as px
from tabulate import tabulate

mydb=mysql.connector.connect(
    host="143.42.63.50",
    user="andy",
    passwd="raconte",
    database="Main"
    )

myc = mydb.cursor()
# myc.execute("select * from Credit")
# myres = myc.fetchall()
# for x in myres:
#     print(x)

# request = "SHOW columns FROM Etablissement"

# cursor.execute(request)
# myres = cursor.fetchall()

# print(column[0] for column in myres)

# mydb.close()

"""
    Etablissements gérés par le ministère de l'Education
"""
request1 = "SELECT * FROM Etablissement WHERE id_tutelle = (SELECT id FROM organisme_tutelle where lower(nom_organisme) = \"ministère chargé de l'éducation nationale et de la jeunesse\");"
myc.execute(request1)
myres = myc.fetchall()
for x in myres:
    print(x)