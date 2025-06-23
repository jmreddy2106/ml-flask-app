from flask import Flask, request, jsonify
import pandas as pd
from ml_model import load_model, predict_species

app = Flask(__name__)
model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame([data])
    prediction = predict_species(model, df)
    return jsonify({'species': prediction})

