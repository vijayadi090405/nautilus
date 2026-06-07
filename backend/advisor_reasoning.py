def generate_advisor_reasoning(design, mission):

    reasons = []
    tradeoffs = []

    detection = design.get("detection", 0)
    drag = design.get("drag", 0)
    survivability = design.get("survivability", 0)

    material = design.get("material", "")
    propulsion = design.get("propulsion", "")
    coating = design.get("coating", "")

    # -----------------------------------
    # Stealth reasoning
    # -----------------------------------

    if detection < 20:

        reasons.append(
            "Very low predicted detection probability supports covert operations."
        )

    elif detection < 40:

        reasons.append(
            "Moderate detectability balances stealth and performance."
        )

    else:

        tradeoffs.append(
            "Higher detection probability may expose the platform earlier."
        )

    # -----------------------------------
    # Drag reasoning
    # -----------------------------------

    if drag < 1000:

        reasons.append(
            "Low hydrodynamic drag improves efficiency and endurance."
        )

    elif drag > 3000:

        tradeoffs.append(
            "High drag increases propulsion power requirements."
        )

    # -----------------------------------
    # Survivability
    # -----------------------------------

    if survivability > 90:

        reasons.append(
            "Excellent structural survivability margin."
        )

    elif survivability > 75:

        reasons.append(
            "Good pressure resistance for deep-water missions."
        )

    else:

        tradeoffs.append(
            "Lower survivability reduces safety margin."
        )

    # -----------------------------------
    # Material
    # -----------------------------------

    if material == "Titanium":

        reasons.append(
            "Titanium provides high strength with low magnetic signature."
        )

        tradeoffs.append(
            "Titanium increases manufacturing cost."
        )

    elif material == "Composite":

        reasons.append(
            "Composite hull minimizes acoustic and magnetic signatures."
        )

    elif material == "Steel":

        reasons.append(
            "Steel provides excellent robustness."
        )

        tradeoffs.append(
            "Steel increases magnetic observability."
        )

    # -----------------------------------
    # Propulsion
    # -----------------------------------

    if propulsion == "Electric":

        reasons.append(
            "Electric propulsion minimizes acoustic signature."
        )

    elif propulsion == "Pump-Jet":

        reasons.append(
            "Pump-jet propulsion reduces cavitation risk."
        )

    else:

        tradeoffs.append(
            "Conventional propulsion increases detectability."
        )

    # -----------------------------------
    # Coating
    # -----------------------------------

    if coating == "Anechoic":

        reasons.append(
            "Anechoic coating reduces sonar reflections."
        )

    # -----------------------------------
    # Mission specific
    # -----------------------------------

    if mission == "Anti-Submarine":

        reasons.append(
            "Configuration optimized for stealth and sonar evasion."
        )

    elif mission == "Deep Strike":

        reasons.append(
            "Configuration prioritizes range and survivability."
        )

    elif mission == "Coastal Defense":

        reasons.append(
            "Configuration optimized for rapid tactical deployment."
        )

    return {
        "reasons": reasons,
        "tradeoffs": tradeoffs
    }


    if design.get(
        "riskAnalysis"
    ):

        risk = (
            design["riskAnalysis"]
            ["riskLevel"]
        )

        reasons.append(

            f"Monte Carlo analysis indicates {risk} operational risk."

        )