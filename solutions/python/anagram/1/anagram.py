def find_anagrams(word, candidates):
    lst = []
    for item in candidates:
        count = 0
        if item.lower() == word.lower():
            continue
        if len(item) != len(word):
            continue
        temp = list(item.lower())
        for letter in word.lower():
            if letter in temp:
                temp.remove(letter)
            else:
                break
        else:
            lst.append(item)
    return lst
                
