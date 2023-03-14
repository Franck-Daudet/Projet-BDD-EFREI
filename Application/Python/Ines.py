import mysql.connector
import plotly.express as px

mydb=mysql.connector.connect(
    host="143.42.63.50",
    user="ines",
    passwd="mbap",
    database="Main"
    )
request= "select * from Etablissement where lower(commune) <>'paris';"
request_Etablissement_EduNat = "SELECT * FROM Etablissement WHERE id_tutelle = (SELECT id FROM organisme_tutelle where lower(nom_organisme) = \"ministère chargé de l'éducation nationale et de la jeunesse\");"

myc = mydb.cursor()
myc.execute(request)
myres = myc.fetchall()
for x in myres:
    print(x)