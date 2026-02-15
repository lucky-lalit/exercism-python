def value(colors):
    colo_list = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    count = 0
    temp1 = None
    temp2 = None
    for color in colors:
        count = count + 1
        if count == 1:
            temp1=colo_list.index(color)
            continue
        if count == 2:
            temp2 = colo_list.index(color)
            break
    result = str(temp1) + str(temp2)
    return int(result)
            
        
         # temp1=colo_list.index[color]
         # str(temp1)
         # result = result + temp 
         
        
