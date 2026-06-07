def generate_recommendations(metrics):

    recommendations = []

    detection = metrics["detection"]

    sf = metrics["safetyFactor"]

    cavitation = metrics["cavitationRisk"]

    acoustic = metrics["acousticSignature"]

    thermal = metrics["thermalSignature"]

    magnetic = metrics["magneticSignature"]

    drag = metrics["drag"]

    power = metrics["powerRequired"]

    # Detection

    if detection > 50:

        recommendations.append(
            "High detection probability observed. Consider Electric propulsion and anechoic coating."
        )

    elif detection > 20:

        recommendations.append(
            "Moderate sonar detectability. Acoustic reduction measures are recommended."
        )

    else:

        recommendations.append(
            "Sonar detectability remains within acceptable limits."
        )

    # Structural

    if sf < 3:

        recommendations.append(
            "Hull safety margin is low. Increase hull thickness or use Titanium alloy."
        )

    elif sf < 5:

        recommendations.append(
            "Structural margin is acceptable but limited for deep-water operations."
        )

    else:

        recommendations.append(
            "Hull structural safety margin is satisfactory."
        )

    # Cavitation

    if cavitation == "HIGH":

        recommendations.append(
            "Cavitation onset detected. Reduce speed or use Pump-Jet propulsion."
        )

    elif cavitation == "MEDIUM":

        recommendations.append(
            "Approaching cavitation threshold. Monitor high-speed operation."
        )

    else:

        recommendations.append(
            "Cavitation risk remains low."
        )

    # Acoustic

    if acoustic == "HIGH":

        recommendations.append(
            "Acoustic signature is elevated. Stealth performance may be degraded."
        )

    # Thermal

    if thermal == "HIGH":

        recommendations.append(
            "Thermal signature may increase IR detectability."
        )

    # Magnetic

    if magnetic == "HIGH":

        recommendations.append(
            "Steel hull increases magnetic anomaly detection risk."
        )

    # Power

    if power > 300:

        recommendations.append(
            "Power demand is high. Endurance may become mission-limiting."
        )

    # Drag

    if drag > 5000:

        recommendations.append(
            "Hydrodynamic drag is significant. Consider reducing diameter."
        )

    return recommendations