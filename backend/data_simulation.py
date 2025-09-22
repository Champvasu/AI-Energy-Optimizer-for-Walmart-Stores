#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 20:24:44 2025

@author: ashwanthelangovan
"""

import numpy as np
import pandas as pd

def simulate_energy_data(n_hours=24*30, seed=42):
    np.random.seed(seed)
    hours = np.arange(n_hours)
    df = pd.DataFrame({
        'hour': hours % 24,
        'day' : hours // 24,
    })
    df['is_weekend'] = df['day'] % 7 >= 5
    df['temperature'] = (
        25 + 10 * np.sin(2*np.pi*df['hour']/24)
        + np.random.normal(0,2,n_hours)
    )
    df['occupancy'] = (
        (np.sin(2*np.pi*(df['hour']-12)/24)+1)*50
        + np.random.normal(0,10,n_hours)
    )
    df['energy_usage'] = (
        200
        + 5*df['temperature']
        + 2*df['occupancy']
        + df['is_weekend']*20
        + np.random.normal(0,10,n_hours)
    )
    return df

if __name__ == "__main__":
    df = simulate_energy_data()
    df.to_csv("simulated_energy.csv", index=False)
    print("✅ simulated_energy.csv created")