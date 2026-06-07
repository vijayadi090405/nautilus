import math


def transmission_loss(
    distance_km
):

    distance_m = max(
        distance_km * 1000,
        1
    )

    spreading = (
        20 *
        math.log10(
            distance_m
        )
    )

    absorption = (
        0.04 *
        distance_km
    )

    return (
        spreading +
        absorption
    )


def signal_excess(

    source_level,

    distance_km,

    target_strength,

    ambient_noise,

    directivity_index,

    detection_threshold

):

    tl = transmission_loss(
        distance_km
    )

    return (

        source_level

        - tl

        + target_strength

        - (
            ambient_noise
            -
            directivity_index
        )

        - detection_threshold

    )


def detection_probability(
    se
):

    se = max(
        -60,
        min(
            60,
            se
        )
    )

    probability = (

        100 /

        (
            1 +
            math.exp(
                -0.22 *
                se
            )
        )

    )

    return round(
        probability,
        2
    )