def source_level(
    propulsion: str,
    speed_knots: float,
    coating: str = "None"
) -> float:

    propulsion_key = str(
        propulsion
    ).strip()

    base_levels = {

        "Electric": 82.0,

        "Pump-Jet": 90.0,

        "Thermal": 98.0,

    }

    cavitation_thresholds = {

        "Electric": 52.0,

        "Pump-Jet": 58.0,

        "Thermal": 45.0,

    }

    base = base_levels.get(
        propulsion_key,
        90.0
    )

    threshold = cavitation_thresholds.get(
        propulsion_key,
        55.0
    )

    sl = (
        base +
        (0.35 * speed_knots)
    )

    if speed_knots > threshold:

        sl += (
            speed_knots -
            threshold
        ) * 1.6

    if coating == "Basic":

        sl -= 3

    elif coating == "Anechoic":

        sl -= 8

    return round(sl, 2)