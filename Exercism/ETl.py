def transform(legacy_data):
    new_dict  = {}
    for i , value in legacy_data.items():
        for j in value:
            new_dict[j.lower()] = i
    return new_dict
print(transform({1: ["A", "E", "I", "O", "U"]}))