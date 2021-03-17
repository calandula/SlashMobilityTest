import DatabaseConnection
import json

f = open('./settings.json')

settings = json.load(f)["local"]

print(settings)
print(settings["neo4j_user"])

graphdb = GraphDatabase.driver(uri=settings["neo4j_url"], auth=(settings["neo4j_user"], settings["neo4j_password"]))

session = graphdb.session()

q1 = "MATCH (x) return (x)"
nodes = session.run(q1)

for node in nodes:
    print(node)

