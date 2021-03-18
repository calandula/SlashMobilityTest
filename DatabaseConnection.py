from neo4j import GraphDatabase

#Clase encargada de conectarse a una instancia de SGBD Neo4j
class DatabaseConnection:

    def __init__(self, uri, name, password):
        self.uri = uri
        self.name = name
        self.password = password
        self.createSession()

    def createSession(self):
        graphDB = GraphDatabase.driver(self.uri, auth=(self.name, self.password))
        self.session = graphDB.session()

    def executeQuery(self, query):
        return self.session.run(q1)


    
