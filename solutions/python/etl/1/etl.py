def transform(legacy_data):
    new_dict = {}
    for score,letter in legacy_data.items():
        print('i')
        for char in letter:
            print(letter)
            char = char.lower()
            new_dict[char] = score
    return new_dict