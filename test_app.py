from fastapi.testclient import TestClient
from main import app

from datetime import datetime,time

# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"ping": "pong"}


# test to check if Iris Virginica is classified correctly
def test_pred_virginica():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 3.2,
        "sepal_width": 5.2,
        "petal_length": 3.2,
        "petal_width": 4.4,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json()["flower_class"] == "Iris Virginica"

# test to check if Iris Setosa is classified correctly
def test_pred_setosa():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json()["flower_class"] ==  "Iris Setosa"


# test to check if invalid param in payload is passed
def test_pred_invalid_payload():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 2,
        "sepal_wid": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 422
        assert response.json() == {'detail': [{'loc': ['body', 'sepal_width'], 'msg': 'field required', 'type': 'value_error.missing'}]}


# test to check if Iris Virginica is classified correctly with different payload
def test_pred_virginica_diff_payload():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 0.2,
        "sepal_width": 5.4,
        "petal_length": 10.4,
        "petal_width": 6.2,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json()["flower_class"] == "Iris Virginica"

