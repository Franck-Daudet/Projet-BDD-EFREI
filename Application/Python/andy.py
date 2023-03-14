import mysql.connector
import plotly.express as px

mydb=mysql.connector.connect(
    host="143.42.63.50",
    user="andy",
    passwd="raconte",
    database="Main"
    )

myc = mydb.cursor()
myc.execute("select * from Credit")
myres = myc.fetchall()
for x in myres:
    print(x)