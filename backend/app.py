from flask import Flask, request, jsonify
from flask_cors import CORS
from advisor import recommend_design
from advisor_ml import recommend_ml
from explainer import generate_reasoning
from optimizer import optimize_design

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"status": "Nautilus API Running"}

@app.route("/simulate", methods=["POST"])
def simulate():

    data = request.json

    diameter = float(data["diameter"])
    length = float(data["length"])
    weight = float(data["weight"])
    speed = float(data["speed"])
    propulsion = data["propulsion"]

    stability = max(
        0,
        100 - abs(length - (diameter * 8)) * 8
    )

    efficiency = min(
        100,
        (speed * 1.5) - (weight / 150)
    )

    acoustic_risk = (
        diameter * 25
    ) + (
        speed * 0.4
    )

    if propulsion == "Electric":
        acoustic_risk *= 0.7

    elif propulsion == "Pump-Jet":
        acoustic_risk *= 0.8

    acoustic_risk = min(
        acoustic_risk,
        100
    )

    detection_risk = (
        acoustic_risk * 0.7
    ) + (
        diameter * 15
    )

    detection_risk = min(
        detection_risk,
        100
    )

    mission_score = (
        stability * 0.3
        + efficiency * 0.3
        + (100 - acoustic_risk) * 0.2
        + (100 - detection_risk) * 0.2
    )

    return jsonify({

        "stability":
            round(stability, 2),

        "efficiency":
            round(efficiency, 2),

        "acousticRisk":
            round(acoustic_risk, 2),

        "detectionRisk":
            round(detection_risk, 2),

        "missionScore":
            round(mission_score, 2)

    })

@app.route("/advisor", methods=["POST"])
def advisor():

    data = request.json

    mission_map = {
        "Anti-Submarine": 0,
        "Coastal Defense": 1,
        "Deep Strike": 2
    }

    stealth_map = {
        "Low": 0,
        "Medium": 1,
        "High": 2
    }

    depth_map = {
        "Shallow": 0,
        "Deep": 1
    }

    result = recommend_ml(
        mission_map[data["missionType"]],
        stealth_map[data["stealth"]],
        depth_map[data["depth"]],
        int(data["range"]),
    )

    optimization = optimize_design(
    int(data["range"]),
    data["stealth"],
    data["depth"]
)

    result["reasoning"] = generate_reasoning(
    data["missionType"],
    data["stealth"],
    data["depth"],
    int(data["range"]),
    result["propulsion"]
)

    result["alternatives"] = (
    optimization["alternatives"]
)

    result["bestStealth"] = (
    optimization["bestStealth"]
)

    result["bestSpeed"] = (
    optimization["bestSpeed"]
)

    result["bestRange"] = (
    optimization["bestRange"]
)

    return jsonify(result)

@app.route(
    "/optimize",
    methods=["POST"]
)
def optimize():

    data = request.json

    result = optimize_design(
        int(data["range"]),
        data["stealth"],
        data["depth"]
    )

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)