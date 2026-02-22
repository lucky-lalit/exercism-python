def abbreviate(words):
    words = words.upper()
    result = ''
    phrase = words.replace('-',' ').replace('_',' ')
    lst = phrase.split()
    for i in lst:
        result = result + i[0]
    return result
