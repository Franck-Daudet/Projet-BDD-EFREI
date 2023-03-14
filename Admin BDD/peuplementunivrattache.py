import mysql.connector
import plotly.express as px

mydb=mysql.connector.connect(
    host="XXX",
    user="XXX",
    passwd="XXX",
    database="XXX",
    )

myc = mydb.cursor()
myc.execute("select E.id,E2.id from Etablissement E left join Etablissement E2 on E.nom = E2.id_univrattachement;")
myres = myc.fetchall()
for x in myres:
    id = x[0]
    temp =  str(x[1]).split(" | ")
    for e in temp :
        val = "Null"
        if e != "None":
            val = "\""+ str(e) + "\"" 
        myc.execute("INSERT INTO univrattache (idetablissement, idetablissementlie) values ('" + str(id) + "'," + str(val) + ");")
        myc.execute("commit;")

        print("INSERT INTO univrattache (idetablissement, idetablissementlie) values ('" + str(id) + "'," + str(val) + ")")
        myres = myc.fetchall()

