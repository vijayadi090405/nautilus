import math

SEA_WATER_DENSITY = 1025.0
GRAVITY = 9.81


def pressure_at_depth(depth_m):

    return (
        SEA_WATER_DENSITY *
        GRAVITY *
        max(depth_m, 0)
    )


def hoop_stress(
    pressure,
    radius,
    thickness
):

    return (
        pressure *
        radius /
        thickness
    )


def buckling_pressure(
    youngs_modulus,
    poisson,
    thickness,
    radius
):

    return (

        (
            2 *
            youngs_modulus
        )

        /

        (
            math.sqrt(
                3 *
                (
                    1 -
                    poisson**2
                )
            )
        )

        *

        (
            thickness /
            radius
        )**3

    )


def collapse_depth(
    collapse_pressure
):

    return (

        collapse_pressure

        /

        (
            SEA_WATER_DENSITY *
            GRAVITY
        )

    )


def safety_factor(
    material_yield,
    youngs_modulus,
    poisson,
    depth_m,
    hull_radius_m=0.4,
    hull_thickness_m=0.025
):

    pressure = pressure_at_depth(
        depth_m
    )

    hoop = hoop_stress(
        pressure,
        hull_radius_m,
        hull_thickness_m
    )

    yield_sf = (
        material_yield /
        max(hoop, 1)
    )

    critical_pressure = buckling_pressure(
        youngs_modulus,
        poisson,
        hull_thickness_m,
        hull_radius_m
    )

    buckling_sf = (
        critical_pressure /
        max(pressure, 1)
    )

    return min(
        yield_sf,
        buckling_sf
    )