def cavitation_risk(
    propulsion,
    speed_knots
):

    limits = {

        "Electric": 50,

        "Pump-Jet": 60,

        "Thermal": 45

    }

    limit = limits[
        propulsion
    ]

    if speed_knots < (
        limit * 0.8
    ):
        return "LOW"

    if speed_knots < limit:
        return "MEDIUM"

    return "HIGH"