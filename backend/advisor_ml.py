import joblib

rf_model = joblib.load(
    "rf_model.pkl"
)

gb_model = joblib.load(
    "gb_model.pkl"
)

def recommend_ml(
    mission,
    stealth,
    depth,
    range_km
):

    mission_map = {

        "Anti-Submarine":0,

        "Heavy Strike":1,

        "Mine Warfare":2,

        "Coastal Defense":3
    }

    features = [[

        mission_map.get(
            mission,
            0
        ),

        range_km,

        stealth,

        depth
    ]]

    rf_prediction = rf_model.predict(
        features
    )[0]

    gb_prediction = gb_model.predict(
        features
    )[0]

    prediction = (

        rf_prediction +
        gb_prediction

    ) / 2

    diameter = round(
        float(prediction[0]),
        2
    )

    length = round(
        float(prediction[1]),
        2
    )

    speed = round(
        float(prediction[2]),
        2
    )

    mass = round(
        float(prediction[3]),
        2
    )

    if stealth == 2:

        propulsion = "Electric"
        material = "Composite"
        coating = "Anechoic"

    elif stealth == 1:

        propulsion = "Pump-Jet"
        material = "Titanium"
        coating = "Basic"

    else:

        propulsion = "Thermal"
        material = "Steel"
        coating = "None"
    confidence = 85

    if range_km > 120:
        confidence -= 10

    if stealth == 2:
        confidence += 5

    confidence = max(
        50,
        min(
            95,
            confidence
        )
    )

    reasoning = []

    if propulsion == "Electric":
        reasoning.append(
            "ML selected Electric propulsion due to stealth priority."
        )

    if material == "Composite":
        reasoning.append(
            "ML selected Composite hull for low observability."
        )

    if stealth == 2:
        reasoning.append(
            "High-stealth mission strongly influenced design selection."
        )

    if range_km > 100:
        reasoning.append(
            "Extended range requirement increased vehicle size."
        )

    return {
        "confidence": confidence,
        "reasoning": reasoning,
        "diameter": diameter,
        "length": length,
        "speed": speed,
        "mass": mass,
        "material": material,
        "propulsion": propulsion,
        "coating": coating,
        "mission": mission
    }