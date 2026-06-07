from flask import Flask, request, jsonify
from flask_cors import CORS
from advisor import recommend_design
from advisor_ml import recommend_ml
from explainer import generate_reasoning
from mission_simulator import simulate_mission
from advisor_reasoning import (
    generate_advisor_reasoning
)
from monte_carlo import (
    monte_carlo_analysis
)
from optimizer import optimize_design
from optimizer import optimize_design
from assessment import generate_recommendations
from target import (
    target_strength
)
from mission_simulator import (
    simulate_mission
)
from environment import (

    ambient_noise,

    directivity_index,

    detection_threshold

)


app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"status": "Nautilus API Running"}

@app.route("/simulate", methods=["POST"])

def simulate():
    from signatures import (

        acoustic_index,

        magnetic_index,

        thermal_index

    )   
    
    from physics import (
        drag_force,
        hydrodynamic_report
    )
    from acoustics import source_level
    from sonar import signal_excess, detection_probability
    from structure import (
        safety_factor,
        buckling_pressure,
        collapse_depth
    )
    from hull import (
    hull_mass
)
    from materials import MATERIALS
    from energy import (
    power_required,
    stored_energy,
    endurance_hours,
    mission_range_km
)
    from cavitation import (
    cavitation_risk
)

    data = request.json

    diameter = float(data["diameter"])
    length = float(data["length"])
    speed = float(data["speed"])

    propulsion = data["propulsion"]
    material = data["material"]
    coating = data["coating"]

    drag = drag_force(diameter, length, speed)
    hydro = hydrodynamic_report(
        diameter,
        length,
        speed
    )
    sl = source_level(propulsion, speed)
    ts = target_strength(
        diameter,
        length
    )

    nl = ambient_noise(
        3
    )

    di = directivity_index()

    dt = detection_threshold()

    se = signal_excess(

        source_level=sl,

        distance_km=5,

        target_strength=ts,

        ambient_noise=nl,

        directivity_index=di,

        detection_threshold=dt

    )
    detection = detection_probability(se)

    depth_m = 500

    material_props = MATERIALS[material]

    sf = safety_factor(

        material_props["yield"],

        material_props["youngs_modulus"],

        material_props["poisson"],

        depth_m,

        hull_radius_m=
        diameter / 2,

        hull_thickness_m=
        max(
            0.02,
            diameter * 0.03
        )

    )

    import math

    volume = (

        math.pi *

        (diameter / 2) ** 2 *

        length

    )

    thickness_m = max(
        0.02,
        diameter * 0.03
    )

    mass = hull_mass(
        diameter,
        length,
        thickness_m,
        material_props["density"]
    )

    power = power_required(
        drag,
        speed,
        propulsion
    )

    energy = stored_energy(
        propulsion,
        mass
    )

    endurance = endurance_hours(
        energy,
        power
    )

    range_km = mission_range_km(
        endurance,
        speed
    )

    displacement = (
        volume *
        1025
    )
    
    collapse_pressure_value = (
        buckling_pressure(
            material_props["youngs_modulus"],
            material_props["poisson"],
            max(
                0.02,
                diameter * 0.03
            ),
            diameter / 2
        )
    )

    depth_rating = round(
        collapse_depth(
            collapse_pressure_value
        ),
        0
    )
    acoustic_sig = acoustic_index(sl)

    magnetic_sig = magnetic_index(material)

    thermal_sig = thermal_index(propulsion)
    cavitation = (
        cavitation_risk(
            propulsion,
            speed
        )
    )

    risk = "LOW"

    if detection > 40:
        risk = "MEDIUM"

    if detection > 70:
        risk = "HIGH"

    transit_time = (
        ((length * speed) / 8) * 1000
    ) / (speed * 0.514)

    recommendations = generate_recommendations({

        "detection": detection,

        "safetyFactor": sf,

        "cavitationRisk": cavitation,

        "acousticSignature": acoustic_sig,

        "thermalSignature": thermal_sig,

        "magneticSignature": magnetic_sig,

        "drag": drag,

        "powerRequired": power / 1000

    })
    return jsonify({
        "drag": round(drag, 2),
        "sourceLevel": round(sl, 2),
        "signalExcess": round(se, 2),
        "detection": round(detection, 2),
        "safetyFactor": round(sf, 2),
"riskLevel": risk,

"material": material,

"propulsion": propulsion,

"coating": coating,

"transitTime":
round(
    transit_time / 60,
    2
),
"mass":
round(
    mass,
    2
),

"displacement":
round(
    displacement,
    2
),

"powerRequired":
round(
    power/1000,
    2
),

"storedEnergy":
round(
    energy,
    2
),

"endurance":
round(
    endurance,
    2
),

"estimatedRange":
round(
    range_km,
    2
),

"depthRating":
depth_rating,
"collapseDepth":
depth_rating,

"bucklingSafetyFactor":
round(
    sf,
    2
),
"acousticSignature":
acoustic_sig,

"magneticSignature":
magnetic_sig,

"thermalSignature":
thermal_sig,

"recommendations":
recommendations,

"cavitationRisk":
cavitation,

"targetStrength":
round(
    ts,
    2
),

"ambientNoise":
round(
    nl,
    2
),

"directivityIndex":
round(
    di,
    2
),

"detectionThreshold":
round(
    dt,
    2
),
"reynoldsNumber":
round(
    hydro["reynoldsNumber"],
    2
),

"frictionCoefficient":
round(
    hydro["frictionCoefficient"],
    5
),

"wettedSurfaceArea":
round(
    hydro["wettedSurfaceArea"],
    2
),

"formFactor":
round(
    hydro["formFactor"],
    3
),

"frictionResistance":
round(
    hydro["frictionResistance"],
    2
),

"waveResistance":
round(
    hydro["waveResistance"],
    2
),

"totalResistance":
round(
    hydro["totalResistance"],
    2
),

"hydrodynamicEfficiency":
round(
    hydro["hydrodynamicEfficiency"],
    2
),
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
    optimization = optimize_design(
        int(data["range"]),
        data["stealth"],
        data["depth"],
        data["missionType"]
    )
    print("OPTIMIZER OUTPUT")
    print(optimization)

    result = optimization["best"]

    result["alternatives"] = (
        optimization["alternatives"]
    )
    for alt in result["alternatives"]:

        alt_reasoning = generate_advisor_reasoning(
            alt,
            data["missionType"]
        )

        alt["reasoning"] = (
            alt_reasoning["reasons"]
        )

        alt["tradeoffs"] = (
            alt_reasoning["tradeoffs"]
        )

        alt_confidence = 70

        if alt["detection"] < 30:
            alt_confidence += 10

        if alt["survivability"] > 85:
            alt_confidence += 10

        if alt["drag"] < 2000:
            alt_confidence += 5

        alt["confidence"] = min(
            alt_confidence,
            95
        )
    result["warnings"] = (
        optimization["warnings"]
    )

    result["categoryWinners"] = (
        optimization["categoryWinners"]
    )

    result["selectionReason"] = (
        optimization["selectionReason"]
    )
    advisor_reasoning = (
        generate_advisor_reasoning(
            result,
            data["missionType"]
        )
    )

    result["reasoning"] = (
        advisor_reasoning["reasons"]
    )

    result["tradeoffs"] = (
        advisor_reasoning["tradeoffs"]
    )
    confidence = 70

    if result["detection"] < 30:
        confidence += 10

    if result["survivability"] > 85:
        confidence += 10

    if result["drag"] < 2000:
        confidence += 5

    confidence = min(
        confidence,
        95
    )

    result["confidence"] = confidence

    return jsonify(result)

@app.route(
    "/mission",
    methods=["POST"]
)
def mission():

    data = request.json

    result = simulate_mission(
        data["design"],
        data["missionType"]
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
@app.route(
    "/risk-analysis",
    methods=["POST"]
)
def risk_analysis():

    data = request.json

    result = monte_carlo_analysis(

        data["design"],

        data["missionType"],

        data.get(
            "iterations",
            500
        )
    )

    return jsonify(result)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
