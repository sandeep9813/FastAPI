import os
import pandas as pd
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


# -----------------------------
# Paths (robust - no ../ issues)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "../data/Cardiovascular_Disease.csv")
MODEL_PATH = os.path.join(BASE_DIR, "../model/cardio_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "../model/scaler_model.pkl")


# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv(DATA_PATH)

# basic cleaning
df = df[(df['ap_hi'] >= 120) & (df['ap_hi'] <= 210)]
df = df[(df['ap_lo'] >= 50) & (df['ap_lo'] <= 100)]


# -----------------------------
# TRAIN MODEL
# -----------------------------
def cardio_predict():

    features = [
        'age', 'height', 'weight', 'ap_hi', 'ap_lo',
        'cholesterol', 'gluc', 'smoke', 'alco', 'active'
    ]

    target = 'cardio'

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # scaler
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # model
    model = LogisticRegression(
        solver='liblinear',
        class_weight='balanced',
        random_state=42
    )

    model.fit(X_train_scaled, y_train)

    # save correct objects
    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)

    print("Model and scaler saved successfully")

    return model, scaler


# -----------------------------
# LOAD MODEL + SCALER
# -----------------------------
def load_model_scaler():

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    return model, scaler


# run training if file executed directly
if __name__ == "__main__":
    cardio_predict()