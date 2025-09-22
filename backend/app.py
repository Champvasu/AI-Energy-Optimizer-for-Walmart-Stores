#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 20:23:32 2025

@author: ashwanthelangovan
"""

from flask import Flask, request, jsonify
import math

app = Flask(__name__)

# ─── Simple rule-based predictor (no ML dependency) ─────────────────────────────
def rule_based_predict(hour, temperature, occupancy, is_weekend):
	# Base load
	base = 200.0
	# Temperature contributes positively
	temp_component = 5.0 * float(temperature)
	# Occupancy contributes positively
	occ_component = 2.0 * float(occupancy)
	# Weekend uplift
	weekend_component = 20.0 * (1 if int(is_weekend) else 0)
	# Mild hour-of-day modulation (peak around afternoon)
	hour_component = 10.0 * math.sin(2 * math.pi * (float(hour) - 12.0) / 24.0)
	return base + temp_component + occ_component + weekend_component + hour_component

# ─── 1) PREDICTION ENDPOINT ─────────────────────────────────────────────────────
@app.route("/predict", methods=["POST"])
def predict():
	data = request.get_json()
	hour = data["hour"]
	temperature = data["temperature"]
	occupancy = data["occupancy"]
	is_weekend = data["is_weekend"]
	pred = rule_based_predict(hour, temperature, occupancy, is_weekend)
	return jsonify({"predicted_usage_kW": round(float(pred), 2)})

# ─── 2) IN‐MEMORY SENSOR STATE ───────────────────────────────────────────────────
sensor_data = {
	"occupancy": 0,
	"power_kW": None
}

# ─── 3) UPDATE ROUTE (called by sensor_feed.py) ────────────────────────────────
@app.route("/sensor_update", methods=["POST"])
def sensor_update():
	global sensor_data
	sensor_data = request.get_json()
	return jsonify({"status": "ok"}), 200

# ─── 4) READ ROUTE (called by streamlit_app.py) ────────────────────────────────
@app.route("/current_status", methods=["GET"])
def current_status():
	return jsonify(sensor_data), 200

# ─── 5) MAIN LAUNCH ────────────────────────────────────────────────────────────
if __name__ == "__main__":
	# Print your routes so you can verify they’re registered
	print("\n>>> Registered routes:")
	for rule in app.url_map.iter_rules():
		methods = ",".join(sorted(rule.methods - {"HEAD","OPTIONS"}))
		print(f"  {methods:10}  {rule}")
	print()
	app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)