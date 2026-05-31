def recommend_design(
    mission_type,
    range_km,
    stealth,
    depth
):

    if stealth == "High":

        propulsion = "Electric"
        diameter = 0.5
        speed = 40

    else:

        propulsion = "Thermal"
        diameter = 0.7
        speed = 60

    length = 4 + (range_km / 20)

    weight = (
        length
        * diameter
        * 450
    )

    if depth == "Deep":

        weight *= 1.2

    return {

        "diameter":
            round(diameter, 2),

        "length":
            round(length, 2),

        "weight":
            round(weight, 2),

        "speed":
            round(speed, 2),

        "propulsion":
            propulsion,

        "mission":
            mission_type

    }