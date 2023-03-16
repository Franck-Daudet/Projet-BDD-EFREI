import re
import mysql.connector
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

mydb=mysql.connector.connect(
    host="143.42.63.50",
    user="andy",
    passwd="raconte",
    database="Main"
    )

myc = mydb.cursor()
myc.execute("SELECT academie FROM academie LIMIT 4;")
myres = myc.fetchall()

# for x in myres:
#     print(x)
    

labels = []
for x in myres:
    labels.append(''.join(re.findall(r'[A-Za-z]', str(x))))
for a in labels: 
    print (a)

myc = mydb.cursor()
myc.execute("SELECT COUNT(*) AS \"Nombre d\'établissements\" FROM Etablissement,academie WHERE Etablissement.academie = academie.academie GROUP BY academie.academie limit 4;")
myres = myc.fetchall()

values = []
for x in myres:
    values.append(''.join(re.findall(r'\d', str(x))))
for a in values: 
    print (a)

"""
values = [1234,4567,3548,5959]
"""

# fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
# fig.show()