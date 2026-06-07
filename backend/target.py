def target_strength(
    diameter_m,
    length_m
):

    projected_area = (
        diameter_m *
        length_m
    )

    ts = (

        10 *

        __import__("math")
        .log10(
            projected_area
            + 1
        )

    )

    return round(
        ts,
        2
    )