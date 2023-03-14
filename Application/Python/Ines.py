import mysql.connector
import plotly.express as px

mydb=mysql.connector.connect(
    host="143.42.63.50",
    user="ines",
    passwd="mbap",
    database="Main"
    )
<<<<<<< HEAD
request= "select * from Etablissement where lower(commune) <>'paris';"
myc = mydb.cursor()
myc.execute(request)
=======

myc = mydb.cursor()
myc.execute("select * from Credit")
>>>>>>> main
myres = myc.fetchall()
for x in myres:
    print(x)