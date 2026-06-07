import math

def hull_mass(
    diameter_m,
    length_m,
    thickness_m,
    density
):

    outer_radius = (
        diameter_m / 2
    )

    inner_radius = max(
        outer_radius -
        thickness_m,
        0.01
    )

    hull_volume = (

        math.pi *

        (
            outer_radius**2 -
            inner_radius**2
        ) *

        length_m

    )

    return (
        hull_volume *
        density
    )