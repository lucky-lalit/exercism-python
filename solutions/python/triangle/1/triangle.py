def equilateral(sides):
    if (sides[0] == sides[1] == sides[2]) and sides[1] != 0 :
        return True
    else:
        return False
    
def isosceles(sides):
    sides.sort()
    # print(sides,(sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2]),(sides[0]+ sides[1] > sides[2]),(sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2]) or (sides[0]+ sides[1] > sides[2]))
    if ((sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2])) and (sides[0]+ sides[1] > sides[2]):
        return True
    else:
        return False


def scalene(sides):
    # print(sides)
    sides.sort()
    if (sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]) and (sides[0]+ sides[1] > sides[2]):
        return True
    else:
        return False
