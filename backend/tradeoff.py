def analyze_design(
    selected,
    best
):

    pros = []
    cons = []

    if selected["speed"] >= best["speed"]:
        pros.append(
            "Higher speed capability"
        )
    else:
        cons.append(
            "Lower speed than best design"
        )

    if selected["stealth"] >= best["stealth"]:
        pros.append(
            "Better stealth profile"
        )
    else:
        cons.append(
            "Reduced stealth performance"
        )

    if selected["range"] >= best["range"]:
        pros.append(
            "Longer operational range"
        )
    else:
        cons.append(
            "Lower operational range"
        )

    return {
        "pros": pros,
        "cons": cons
    }