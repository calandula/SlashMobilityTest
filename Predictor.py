import numpy
import pickle
import pandas as pd
from csv import writer
import json
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

def makePrediction(pregnant, glucose, bp, skin, insulin, bmi, pedigree, age):

    model = loadModel("model1")

    if model == -1:
        model = fit()

    probList = model.predict_proba([[pregnant, glucose, bp, skin, insulin, bmi, pedigree, age]])
    
    return {"result": probList} 


#if the user validates our result, we add the new row and we refit the model with the new data
def refit(pregnant, glucose, bp, skin, insulin, bmi, pedigree, age, label):

    append_list_as_row("./archive/diabetes.csv", [pregnant, glucose, bp, skin, insulin, bmi, pedigree, age, label])

    model = fit()

    saveModel(model, "model1")

    
def openFile(filename):

    col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
    return pd.read_csv(filename, header=None, names=col_names)


def loadModel(modelFile):
    try:
        loaded_model = pickle.load(open("./models/" + modelFile + ".sav", 'rb'))
        return loaded_model
    except EOFError:
        return -1

def saveModel(model, modelFile):
    pickle.dump(model, open("./models/" + modelFile + ".sav", 'wb'))

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def fit():

    df = openFile("./archive/diabetes.csv")

    df = df[1:]

    #Feature Selection
    feature_cols = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
    X = df[feature_cols] #Features
    y = df.label #Target variable

    #Splitting Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

    #Build Decision Tree Model
    model = DecisionTreeClassifier()
    model = model.fit(X_train,y_train)
    y_pred = model.predict(X_test)

    saveModel(model, "model1")

    return model


