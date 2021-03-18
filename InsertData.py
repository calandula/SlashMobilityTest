from DatabaseConnection import DatabaseConnection
import json
import pandas as pd

#File that its responsability is inserting nodes of patients into neo4j

#We create the db connection with neo4j
f = open('./settings.json')
settings = json.load(f)["local"]
conn = DatabaseConnection(settings["neo4j_url"], settings["neo4j_user"], settings["neo4j_password"])

#We read csv data
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
pima = pd.read_csv("./archive/diabetes.csv", header=None, names=col_names)

data = pima[1:]
first = True
query = ""

for ind in data.index: 
    print(data['pregnant'][ind] + "and" +  data['glucose'][ind])
    if first:
        query += "CREATE (" + str(ind) + ":pacient { pregnant:" + str(data['pregnant'][ind]) + ", glucose:" + str(data['glucose'][ind])  + ", bp:" + str(data['bp'][ind]) + ", skin:" + str(data['skin'][ind]) + ", insulin:" + str(data['insulin'][ind]) + ", bmi:" + str(data['bmi'][ind]) + ", pedigree:" + str(data['pedigree'][ind]) + ", age:" + str(data['age'][ind]) + ", label:" + str(data['label'][ind]) + "}),"
    else:
        query += "(" + str(ind) + ":pacient { pregnant:" + str(data['pregnant'][ind]) + ", glucose:" + str(data['glucose'][ind])  + ", bp:" + str(data['bp'][ind]) + ", skin:" + str(data['skin'][ind]) + ", insulin:" + str(data['insulin'][ind]) + ", bmi:" + str(data['bmi'][ind]) + ", pedigree:" + str(data['pedigree'][ind]) + ", age:" + str(data['age'][ind]) + ", label:" + str(data['label'][ind]) + "})"
        first = False

    conn.executeQuery(query)


