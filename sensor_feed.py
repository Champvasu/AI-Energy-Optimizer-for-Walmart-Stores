#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 12:12:23 2025

@author: ashwanthelangovan
"""

# sensor_feed.py
import time, random, requests

API = "http://127.0.0.1:5000"

while True:
    data = {
        "occupancy": random.randint(0,200),
        "power_kW": round(random.uniform(400,600),2)
    }
    try:
       resp = requests.post(f"{API}/sensor_update", json=data, timeout=2)
       print("→ sensor_update:", resp.status_code, resp.text)
    except Exception as e:
        print("Error:", e)
    time.sleep(5)