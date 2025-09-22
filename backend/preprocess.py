#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 20:21:11 2025

@author: ashwanthelangovan
"""

import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_split(path="simulated_energy.csv"):
    df = pd.read_csv(path)
    df = pd.get_dummies(df, columns=['is_weekend'], drop_first=True)
    X = df[['hour','temperature','occupancy','is_weekend_True']]
    y = df['energy_usage']
    return train_test_split(X, y, test_size=0.2, random_state=42)

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_and_split()
    print("Train/Test sizes:", X_train.shape, X_test.shape)