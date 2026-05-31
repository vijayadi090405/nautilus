def generate_reasoning(
    mission_type,
    stealth,
    depth,
    range_km,
    propulsion
):

    reasons = []

    reasons.append(
        f"Mission profile: {mission_type}"
    )

    if stealth == "High":
        reasons.append(
            "High stealth requirement detected."
        )

    elif stealth == "Medium":
        reasons.append(
            "Balanced stealth profile selected."
        )

    else:
        reasons.append(
            "Performance prioritized over stealth."
        )

    if depth == "Deep":
        reasons.append(
            "Deep-water operation considered."
        )

    if range_km > 70:
        reasons.append(
            "Long-range mission detected."
        )

    if propulsion == "Electric":
        reasons.append(
            "Electric propulsion minimizes acoustic signature."
        )

    elif propulsion == "Pump-Jet":
        reasons.append(
            "Pump-jet propulsion balances speed and stealth."
        )

    else:
        reasons.append(
            "Thermal propulsion maximizes speed."
        )

    return reasons