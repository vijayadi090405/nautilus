import random
import numpy as np

from mission_simulator import simulate_mission


def monte_carlo_analysis(
    design,
    mission_type,
    iterations=500
):
    mission_scores = []

    detection_values = []

    survivability_values = []

    for _ in range(iterations):

        sample = design.copy()

        sample["detection"] *= random.uniform(
            0.85,
            1.15
        )

        sample["survivability"] *= random.uniform(
            0.90,
            1.10
        )

        sample["estimatedRange"] *= random.uniform(
            0.90,
            1.10
        )

        result = simulate_mission(
            sample,
            mission_type
        )

        mission_scores.append(
            result["missionSuccess"]
        )

        detection_values.append(
            sample["detection"]
        )

        survivability_values.append(
            sample["survivability"]
        )

    mean_success = np.mean(
        mission_scores
    )

    std_success = np.std(
        mission_scores
    )

    p10 = np.percentile(
        mission_scores,
        10
    )

    p90 = np.percentile(
        mission_scores,
        90
    )

    success_rate = (
        sum(
            score > 50
            for score in mission_scores
        )
        / iterations
    ) * 100

    if success_rate > 80:
        risk_level = "LOW"

    elif success_rate > 60:
        risk_level = "MEDIUM"

    else:
        risk_level = "HIGH"

    return {

        "iterations":
        iterations,

        "meanMissionSuccess":
        round(
            mean_success,
            2
        ),

        "stdMissionSuccess":
        round(
            std_success,
            2
        ),

        "p10MissionSuccess":
        round(
            p10,
            2
        ),

        "p90MissionSuccess":
        round(
            p90,
            2
        ),

        "successRate":
        round(
            success_rate,
            2
        ),

        "riskLevel":
        risk_level,

        "meanDetection":
        round(
            np.mean(
                detection_values
            ),
            2
        ),

        "meanSurvivability":
        round(
            np.mean(
                survivability_values
            ),
            2
        )
    }