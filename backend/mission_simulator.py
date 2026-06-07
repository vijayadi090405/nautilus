import random
from mission_profiles import MISSIONS   
def simulate_mission(
    design,
    mission_type
):
    profile = MISSIONS.get(
        mission_type,
        MISSIONS["Anti-Submarine"]
    )

    difficulty = profile["targetDifficulty"]
    environment = profile["environmentFactor"]

    range_score = min(
        design["estimatedRange"] / 50,
        1.0
    )

    stealth_score = (
        1 -
        design["detection"] / 100
    )

    survivability_score = (
        design["survivability"] / 100
    )

    detection_success = (

        0.6 +

        stealth_score * 0.4 *

        random.uniform(
            0.9,
            1.1
        )
    )

    attack_success = (

        0.5 +

        survivability_score * 0.5 *

        random.uniform(
            0.9,
            1.1
        )
    )

    escape_success = (

        0.4 +

        stealth_score * 0.6 *

        random.uniform(
            0.9,
            1.1
        )
    )

    mission_success = (
        detection_success *
        attack_success *
        escape_success *
        range_score *
        environment
        / difficulty
    ) * 100

    return {

        "missionSuccess":
        round(
            mission_success,
            2
        ),

        "targetDetected":
        detection_success > 0.6,

        "attackSuccess":
        attack_success > 0.6,

        "escapeProbability":
        round(
            escape_success * 100,
            2
        ),

        "timeline": [

            {
                "phase":
                "Transit",
                "status":
                "Completed"
            },

            {
                "phase":
                "Search",
                "status":
                "Completed"
            },

            {
                "phase":
                "Attack",
                "status":
                "Completed"
            },

            {
                "phase":
                "Escape",
                "status":
                "Completed"
            }

        ]
    }