def is_isogram(string):
    string = string.upper()
    iterate = 0
    count = 0
    for i in string:
        iterate = iterate + 1
        print(i,string)
        print(65<=ord(i)<=97,ord(i))
        if i in string[iterate:]:
            if 65<=ord(i)<=97:
                break
            else:
                count = count + 1
                pass
        else:
            count=count + 1
    if count == len(string):      
        return True
    else:
        return False
        
        
