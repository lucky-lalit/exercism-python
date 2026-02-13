def label(colors):
    colo_list = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    temp1=None
    temp2=None
    temp3=None
    count = 0
    for color in colors:
        if count == 3:
            break
        count = count + 1
        if count == 1:
            temp1 = colo_list.index(color)
            if temp1 == 0:
                temp1 = ''
            continue
        if count == 2:
            temp2 = colo_list.index(color)
            continue 
        if count == 3:
            temp3 = colo_list.index(color)
    unit = '0'*temp3
    result = str(temp1) + str(temp2) + str(unit)
    # print('debug0',unit)
    # print('debug1',result)
    # print('debug2',result[-1:-7:-1])
    # print('debug3',result[-1:-7:-1]=='000000')
    # print('debug4',(len(result) >= 4 and ((result[-1]==result[-2]==result[-3] == '0') and (result[-4] != 0))))
    # print('debug5',len(result) >= 6 and result[-1:-7:-1]=='000000')
    # print('debug6',result[-4]!=0)
    # print('debug7',result[-1:-9:-1]!='000000000')
    if result[-1:-7:-1]!='000000' and len(result) >= 4 and ((result[-1]==result[-2]==result[-3] == '0') and (result[-4] != 0)):
        return result[:-3]+' kiloohms'
    # print(result)
    if result[-1:-7:-1]=='000000' and len(result)<10:
        return result[:-6]+' megaohms'
    if len(result)<=3 :
        return result +' ohms'
    else:
        return result[:-9] + ' gigaohms'
        
    
