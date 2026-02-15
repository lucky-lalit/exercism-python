def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    elif len(strand_a)<1:
        return 0
    count = 0
    difference = 0
    # print('debug')
    while len(strand_a)>count:
        # print('debug0')
        if strand_a[count]==strand_b[count]:
            pass
        else:
            # print('debug1',difference)
            difference = difference + 1
        count = count +1
    # if difference > 0:
    return difference
    # else:
    #     return 0
        
            
