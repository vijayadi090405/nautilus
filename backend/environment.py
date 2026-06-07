def ambient_noise(
    sea_state=3
):

    return {

        1: 45,

        2: 50,

        3: 55,

        4: 60,

        5: 65

    }.get(
        sea_state,
        55
    )


def directivity_index():

    return 15


def detection_threshold():

    return 10