def generate_reasoning(
    design
):

    reasons = []

    detection = design.get(
        "detection",
        0
    )

    drag = design.get(
        "drag",
        0
    )

    safety_factor = design.get(
        "safetyFactor",
        0
    )

    depth_rating = design.get(
        "depthRating",
        0
    )

    source_level = design.get(
        "sourceLevel",
        0
    )

    power = design.get(
        "powerRequired",
        0
    )

    endurance = design.get(
        "endurance",
        0
    )

    material = design.get(
        "material",
        ""
    )

    propulsion = design.get(
        "propulsion",
        ""
    )

    coating = design.get(
        "coating",
        ""
    )

    acoustic = design.get(
        "acousticSignature",
        0
    )

    magnetic = design.get(
        "magneticSignature",
        0
    )

    thermal = design.get(
        "thermalSignature",
        0
    )

    # DETECTION

    if detection < 20:

        reasons.append(
            f"Predicted detection probability is only {detection:.1f}%, indicating strong survivability in contested waters."
        )

    elif detection < 50:

        reasons.append(
            f"Detection probability of {detection:.1f}% represents a balanced stealth-performance tradeoff."
        )

    else:

        reasons.append(
            f"Detection probability of {detection:.1f}% may expose the platform to early adversary tracking."
        )

    # ACOUSTICS

    reasons.append(
        f"Radiated source level is estimated at {source_level:.1f} dB."
    )

    if acoustic < 0.4:

        reasons.append(
            "Acoustic signature index is low, supporting covert operations."
        )

    elif acoustic < 0.7:

        reasons.append(
            "Acoustic signature is moderate and acceptable for most operational scenarios."
        )

    else:

        reasons.append(
            "Acoustic signature is elevated and may increase passive sonar vulnerability."
        )

    # DRAG

    if drag < 1000:

        reasons.append(
            f"Hydrodynamic drag of {drag:.0f} N supports efficient underwater transit."
        )

    elif drag < 3000:

        reasons.append(
            f"Drag force of {drag:.0f} N remains within acceptable operational limits."
        )

    else:

        reasons.append(
            f"High drag force of {drag:.0f} N significantly increases propulsion demand."
        )

    # POWER

    reasons.append(
        f"Estimated propulsion power requirement is {power:.1f} kW."
    )

    # STRUCTURE

    if safety_factor > 5:

        reasons.append(
            f"Safety factor of {safety_factor:.2f} supports deep-water deployment with substantial structural margin."
        )

    else:

        reasons.append(
            f"Safety factor of {safety_factor:.2f} suggests limited reserve structural margin."
        )

    reasons.append(
        f"Estimated operational depth rating is approximately {depth_rating:.0f} m."
    )

    # MATERIAL

    if material == "Composite":

        reasons.append(
            "Composite construction minimizes magnetic observability and reduces structural mass."
        )

    elif material == "Titanium":

        reasons.append(
            "Titanium provides an excellent balance of strength, corrosion resistance and low magnetic signature."
        )

    elif material == "Steel":

        reasons.append(
            "Steel provides maximum structural robustness but increases magnetic observability."
        )

    # PROPULSION

    if propulsion == "Electric":

        reasons.append(
            "Electric propulsion minimizes thermal and acoustic signatures."
        )

    elif propulsion == "Pump-Jet":

        reasons.append(
            "Pump-jet propulsion reduces cavitation and radiated noise at higher speeds."
        )

    elif propulsion == "Thermal":

        reasons.append(
            "Thermal propulsion maximizes endurance and speed at the expense of detectability."
        )

    # COATING

    if coating == "Anechoic":

        reasons.append(
            "Anechoic coating significantly attenuates sonar reflections and radiated noise."
        )

    elif coating == "Basic":

        reasons.append(
            "Basic acoustic coating provides moderate signature reduction."
        )

    # ENDURANCE

    reasons.append(
        f"Predicted endurance is {endurance:.1f} hours under current operating conditions."
    )

    return reasons