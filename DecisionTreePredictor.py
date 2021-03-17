import numpy
import pickle
import pandas
import json
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
import DatabaseConnection

class DecisionTreePredictor():

    def __init__(self):
         self.newX = [value1, value2, value3, value4, value5]
        
    def loadModel(self, filename = "./models/model1.sav"):
        loaded_model = pickle.load(open(filename, 'rb'))

        if loaded_model:
            self.model = loaded_model
        else:
            self.fitNewModel()

    def getPredictedValues(self):
        y = self.model.predict_proba(self.newX)

    def fitNewModel(self):
        self.model = DecisionTreeClassifier(random_state=0)
        self.model.fit()

    def validateAndRefit(self):

    def getData():
        f = open('./settings.json')
        settings = json.load(f)["local"]
        conn = DatabaseConnection(settings["neo4j_url"], settings["neo4j_user"], settings["neo4j_password"])
        conn.executeQuery()




