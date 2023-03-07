import mysql.connector
import plotly.express as px

mydb=mysql.connector.connect(
    host="XXX",
    user="XXX",
    passwd="XXX",
    database="XXX",
    )

myc = mydb.cursor()
myc.execute("select * from Credit")
myres = myc.fetchall()
for x in myres:
    print (x)
