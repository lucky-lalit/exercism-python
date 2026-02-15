def append(list1, list2):
    new = [0]*(len(list1)+len(list2))
    for i in range(len(list1)):
        new[i] = list1[i]
        # new.append(i)
    for j in range(len(list2)):
        new[j+len(list1)] = list2[j] 
        # new.append(j)
    return new
        


def concat(lists):
    result = []
    for single_list in lists:
        for elem in single_list:
            result.append(elem)
    return result
def filter(function, list):
    # for i in list:
    #     if i%2==1:
    new = []
    for item in list:
        if(function(item)):
            new.append(item)
    return new

def length(list):
    count = 0
    for i in list:
        count = count + 1
    return count


def map(function, list):
    new = []
    for item in list:
        new.append(function(item))
    return new


def foldl(function, list, initial):
    result = initial
    for item in list:
        result = function(result,item)
        # initial = item
    return result

def foldr(function, list, initial):
    result = initial
    for i in range(1,len(list)+1):
        print(i,list[-i])
        result = function(result,list[-i])
    return result

def reverse(list):
    new = []
    for i in range(1,len(list)+1):
        new.append(list[-i])
    return new
