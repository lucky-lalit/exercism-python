
def is_pangram(sentence):
    all_lower_cases = 'abcdefghijklmnopqrstuvwxyz'
    # cond_list = []
    counter = 0
    for c in all_lower_cases:
        if c in sentence.lower():
            counter = counter +1
            # cond_list.append(True)
        # else:
            # cond_list.append(False)
    # return all(cond_list)
    return counter == len(all_lower_cases)
    # for cond in cond_list:
    #     if not cond :
    #         return False

    # return True
            
            
    # return all(letter in sentence.lower() for letter in ascii_lowercase)