from fastapi import FastAPI
from App.schema import Cardio
from App.model import load_model_scaler
import pandas as pd


# object of FastAPI
app = FastAPI()

model, scaler = load_model_scaler()


# get request
@app.get('/')
def home():
    return {"message": "welcome to fastapi application"}


# post method for prediction
@app.post('/cardio-predict')
def predict_cardio(data: Cardio):

    input_data = pd.DataFrame([
        data.model_dump()
    ])

    input_scaler = scaler.transform(input_data)

    prediction = model.predict(input_scaler)[0]

    return {
        'prediction_status': int(prediction),
        'status': 'likely to be healthy' if prediction == 0 else 'likely to be unhealthy'
    }