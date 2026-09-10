def initialize_names(name):
    full_name = name.split()

    if len(full_name) <= 2:
        return " ".join(full_name)

    first_name = full_name[0]
    last_name = full_name[-1]
    middle_name = [f"{n[0].upper()}." for n in full_name[1:-1]]

    return f"{first_name} {' '.join(middle_name)} {last_name}"