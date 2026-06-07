import math

ENERGY_DENSITY = {

    "Electric": 250,      # Li-ion Wh/kg

    "Pump-Jet": 600,      # battery + pump jet system

    "Thermal": 1200       # thermal propulsion equivalent

}
PROPULSION_EFFICIENCY = {

    "Electric": 0.90,

    "Pump-Jet": 0.75,

    "Thermal": 0.60

}

def power_required(
    drag_force_n,
    speed_knots,
    propulsion="Electric"
):

    speed_ms = (
        speed_knots * 0.514444
    )

    shaft_power = (
        drag_force_n *
        speed_ms
    )

    efficiency = (
        PROPULSION_EFFICIENCY[
            propulsion
        ]
    )

    actual_power = (
        shaft_power /
        efficiency
    )

    return actual_power


def stored_energy(
    propulsion,
    mass_kg
):

    energy_fraction = {

        "Electric": 0.18,
        "Pump-Jet": 0.22,
        "Thermal": 0.28

    }[propulsion]

    energy_mass = (
        mass_kg *
        energy_fraction
    )

    energy_density = (
        ENERGY_DENSITY[
            propulsion
        ]
    )

    return (
        energy_mass *
        energy_density
    )




def endurance_hours(
    energy_wh,
    power_w
):

    if power_w <= 0:
        return 0

    return (
        energy_wh /
        power_w
    )


def mission_range_km(
    endurance_hr,
    speed_knots
):

    speed_kmh = (
        speed_knots *
        1.852
    )

    return (
        endurance_hr *
        speed_kmh
    )

def energy_efficiency_score(
    range_km,
    energy_wh
):

    if energy_wh <= 0:
        return 0

    score = (
        range_km /
        (energy_wh / 1000)
    )

    return min(
        100,
        score * 5
    )