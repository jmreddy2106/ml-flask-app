import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_predict_endpoint():
    client = app.test_client()
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post('/predict', json=payload)
    assert response.status_code == 200
    
    data = response.get_json()
    assert 'species' in data
