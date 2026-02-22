def transform(legacy_data):
    new_dict = {}
    for score,letter in legacy_data.items():
        for char in letter:
            new_dict[char.lower()] = score
    return new_dict