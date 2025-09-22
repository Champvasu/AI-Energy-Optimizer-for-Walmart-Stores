#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 20:21:45 2025

@author: ashwanthelangovan
"""

# train_model.py
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib, os
import numpy as np                 # ← add this import
from preprocess import load_and_split

def train_and_save(model_path="models/rf_model.pkl"):
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    X_train, X_test, y_train, y_test = load_and_split()

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)

    # compute RMSE manually instead of using squared=False
    mse = mean_squared_error(y_test, preds)
    rmse = np.sqrt(mse)

    print(f"MAE: {mae:.2f}, RMSE: {rmse:.2f}")

    joblib.dump(model, model_path)
    print(f"✅ Model saved to {model_path}")

if __name__ == "__main__":
    train_and_save()