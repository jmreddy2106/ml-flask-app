import pandas as pd
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ml_model import train_and_save_model, load_model, predict_species

def test_predict_species():
    model = load_model()
    df = pd.DataFrame([{
        'sepal_length': 5.1,
        'sepal_width': 3.5,
        'petal_length': 1.4,
        'petal_width': 0.2
    }])
    species = predict_species(model, df)
    assert species in ['setosa', 'versicolor', 'virginica']


def test_train_and_save_model_creates_file():
    if os.path.exists('iris_model.pkl'):
        os.remove('iris_model.pkl')
    train_and_save_model()
    assert os.path.exists('iris_model.pkl')

def test_load_model_triggers_training_if_missing():
    # Delete model file to force training
    if os.path.exists('iris_model.pkl'):
        os.remove('iris_model.pkl')

    # Now load_model will trigger train_and_save_model()
    model = load_model()

    assert os.path.exists('iris_model.pkl')
    assert model is not None