def factors(value):
    lst = []
    i = 2
    while value > 1:
        if value % i == 0:
            lst.append(i)
            value = value//i
        else:
            i = i + 1
    return lst