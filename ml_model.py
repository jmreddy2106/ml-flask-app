import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_and_save_model():
    iris = load_iris()
    X = iris.data
    y = iris.target
    clf = RandomForestClassifier()
    clf.fit(X, y)
    joblib.dump(clf, 'iris_model.pkl')

def load_model():
    import os
    if not os.path.exists('iris_model.pkl'):
        train_and_save_model()
    clf = joblib.load('iris_model.pkl')
    return clf

def predict_species(model, df):
    required_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    X = df[required_columns].values
    prediction = model.predict(X)
    iris = load_iris()
    return iris.target_names[prediction[0]]
