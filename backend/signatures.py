def acoustic_index(
    source_level
):

    return round(
        source_level / 140,
        2
    )


def magnetic_index(
    material
):

    return {

        "Steel": 1.00,

        "Titanium": 0.45,

        "Composite": 0.10

    }[material]


def thermal_index(
    propulsion
):

    return {

        "Electric": 0.10,

        "Pump-Jet": 0.50,

        "Thermal": 1.00

    }[propulsion]