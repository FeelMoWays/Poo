def resistor_label(colors):
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

    tolerance = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10
    }

    resistance = (
        (values[colors[0]] * 10 + values[colors[1]])
        * (10 ** values[colors[2]])
    )

    if resistance % 1_000_000_000 == 0:
        value = f"{resistance // 1_000_000_000} gigaohms"
    elif resistance % 1_000_000 == 0:
        value = f"{resistance // 1_000_000} megaohms"
    elif resistance % 1_000 == 0:
        value = f"{resistance // 1_000} kiloohms"
    else:
        value = f"{resistance} ohms"

    if colors[3] in tolerance:
        return f"{value} ± {tolerance[colors[3]]}%"
    else:
        return "0 ohms"

print(resistor_label(["blue", "grey", "brown", "violet"]))