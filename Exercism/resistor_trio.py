def label(colors):
    values = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    resistance = (
        (values[colors[0]] * 10 + values[colors[1]])
        * (10 ** values[colors[2]])
    )

    if resistance % 1_000_000_000 == 0:
        return f"{resistance // 1_000_000_000} gigaohms"
    elif resistance % 1_000_000 == 0:
        return f"{resistance // 1_000_000} megaohms"
    elif resistance % 1_000 == 0:
        return f"{resistance // 1_000} kiloohms"
    else:
        return f"{resistance} ohms"