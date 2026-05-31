import joblib

model = joblib.load("model.pkl")

def recommend_ml(
    mission,
    stealth,
    depth,
    range_km
):

    prediction = model.predict([[
        mission,
        stealth,
        depth,
        range_km
    ]])[0]

    diameter = round(float(prediction[0]), 2)
    length = round(float(prediction[1]), 2)
    speed = round(float(prediction[2]), 2)

    if stealth >= 2:
        propulsion = "Electric"
    elif stealth == 1:
        propulsion = "Pump-Jet"
    else:
        propulsion = "Thermal"

    weight = round(
        diameter *
        length *
        450,
        2
    )

    return {
        "diameter": diameter,
        "length": length,
        "speed": speed,
        "weight": weight,
        "propulsion": propulsion
    }