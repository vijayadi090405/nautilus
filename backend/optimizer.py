import random

def optimize_design(
    target_range,
    stealth_priority,
    depth
):

    candidates = []


    for _ in range(100):

        diameter = round(
            random.uniform(0.4, 1.2),
            2
        )

        length = round(
            random.uniform(3, 10),
            2
        )

        weight = round(
    diameter * length * 450,
    0
)

        speed = random.randint(
            30,
            80
        )

        propulsion = random.choice([
            "Electric",
            "Pump-Jet",
            "Thermal"
        ])

        stealth_score = 100

        stealth_score -= (
            diameter * 25
        )

        stealth_score -= (
            speed * 0.4
        )

        if propulsion == "Electric":
            stealth_score += 15

        if propulsion == "Pump-Jet":
            stealth_score += 8

        range_score = max(
            0,
            100 - abs(
                target_range -
                (length * 12)
            )
        )

        speed_score = speed

        mission_score = (
            stealth_score * 0.4 +
            range_score * 0.3 +
            speed_score * 0.3
        )

        candidates.append({

    "diameter":
        diameter,

    "length":
        length,

    "speed":
        speed,
"weight": weight,
    "propulsion":
        propulsion,

    "score":
        round(
            mission_score,
            2
        ),

    "stealth":
        round(
            stealth_score,
            2
        ),

    "range":
        round(
            length * 12,
            2
        ),

    "acousticRisk":
        round(
            100 - stealth_score,
            2
        )
})

    candidates.sort(
        key=lambda x:
        x["score"],
        reverse=True
    )
    
    best_stealth = max(
    candidates,
    key=lambda x:
    x["stealth"]
)

    best_speed = max(
    candidates,
    key=lambda x:
    x["speed"]
)

    best_range = max(
    candidates,
    key=lambda x:
    x["range"]
)

    return {

    "best":
        candidates[0],

    "bestStealth":
        best_stealth,

    "bestSpeed":
        best_speed,

    "bestRange":
        best_range,

    "alternatives":
        candidates[1:6],

    "top10":
        candidates[:10]

}