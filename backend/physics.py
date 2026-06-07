import math

SEA_WATER_DENSITY = 1025.0
WATER_VISCOSITY = 0.00108

KNOT_TO_MS = 0.514444


def speed_ms(speed_knots):
    return speed_knots * KNOT_TO_MS


def reynolds_number(
    speed_knots,
    length_m
):
    v = speed_ms(speed_knots)

    return (
        SEA_WATER_DENSITY
        * v
        * length_m
        / WATER_VISCOSITY
    )


def wetted_surface_area(
    diameter_m,
    length_m
):
    return math.pi * diameter_m * length_m


def friction_coefficient(
    reynolds
):
    if reynolds <= 0:
        return 0

    return (
        0.075 /
        (
            (
                math.log10(reynolds)
                - 2
            ) ** 2
        )
    )


def form_factor(
    diameter_m,
    length_m
):
    ld_ratio = (
        length_m /
        max(diameter_m, 0.01)
    )

    k = max(
        0.08,
        0.6 / ld_ratio
    )

    return k


def friction_resistance(
    diameter_m,
    length_m,
    speed_knots
):
    v = speed_ms(speed_knots)

    re = reynolds_number(
        speed_knots,
        length_m
    )

    cf = friction_coefficient(re)

    surface = wetted_surface_area(
        diameter_m,
        length_m
    )

    rf = (
        0.5
        * SEA_WATER_DENSITY
        * (v ** 2)
        * surface
        * cf
    )

    return rf


def wave_resistance(
    diameter_m,
    length_m,
    speed_knots,
    submerged=True
):
    if submerged:
        return 0

    v = speed_ms(speed_knots)

    return (
        0.01
        *
        SEA_WATER_DENSITY
        *
        (v ** 2)
    )


def total_resistance(
    diameter_m,
    length_m,
    speed_knots,
    submerged=True
):
    rf = friction_resistance(
        diameter_m,
        length_m,
        speed_knots
    )

    k = form_factor(
        diameter_m,
        length_m
    )

    rw = wave_resistance(
        diameter_m,
        length_m,
        speed_knots,
        submerged
    )

    return (
        rf * (1 + k)
        + rw
    )


def hydrodynamic_efficiency(
    diameter_m,
    length_m,
    speed_knots
):
    resistance = total_resistance(
        diameter_m,
        length_m,
        speed_knots
    )

    ld_ratio = (
        length_m /
        max(diameter_m, 0.01)
    )

    score = (
        120
        -
        resistance / 50
        +
        ld_ratio * 2
    )

    return max(
        0,
        min(
            100,
            score
        )
    )


def drag_force(
    diameter_m,
    length_m,
    speed_knots
):
    return total_resistance(
        diameter_m,
        length_m,
        speed_knots
    )


def hydrodynamic_report(
    diameter_m,
    length_m,
    speed_knots
):
    re = reynolds_number(
        speed_knots,
        length_m
    )

    cf = friction_coefficient(re)

    area = wetted_surface_area(
        diameter_m,
        length_m
    )

    k = form_factor(
        diameter_m,
        length_m
    )

    rf = friction_resistance(
        diameter_m,
        length_m,
        speed_knots
    )

    rw = wave_resistance(
        diameter_m,
        length_m,
        speed_knots
    )

    rt = total_resistance(
        diameter_m,
        length_m,
        speed_knots
    )

    return {
        "reynoldsNumber": re,
        "frictionCoefficient": cf,
        "wettedSurfaceArea": area,
        "formFactor": k,
        "frictionResistance": rf,
        "waveResistance": rw,
        "totalResistance": rt,
        "hydrodynamicEfficiency":
        hydrodynamic_efficiency(
            diameter_m,
            length_m,
            speed_knots
        )
    }