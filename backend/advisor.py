from optimizer import optimize_design
from advisor_reasoning import generate_advisor_reasoning
from mission_simulator import simulate_mission
from monte_carlo import (
    monte_carlo_analysis
)

def recommend_design(
    mission_type,
    range_km,
    stealth,
    depth
):

    result = optimize_design(
        target_range=range_km,
        stealth_priority=stealth,
        depth=depth
    )

    best = result["best"]

    best["mission"] = mission_type

    reasoning = generate_advisor_reasoning(
        best,
        mission_type
    )

    best["reasoning"] = reasoning["reasons"]
    best["tradeoffs"] = reasoning["tradeoffs"]

    mission_result = simulate_mission(
        best,
        mission_type
    )

    best["missionSimulation"] = (
        mission_result
    )

    risk_analysis = (
        monte_carlo_analysis(
            best,
            mission_type,
            500
        )
    )

    best["riskAnalysis"] = (
        risk_analysis
    )

    return best