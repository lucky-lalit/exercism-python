def commands(binary_str):
    result = []
    # print(type(binary_str))
    if binary_str[-1]=='1':
        result.append('wink')
        print(result)
        # print(binary_str[-2]=='1')
    if binary_str[-2]=='1':
        result.append('double blink')
        print(result)
    if binary_str[-3]=='1':
        result.append('close your eyes')
    if binary_str[-4]=='1':
        result.append('jump')
    if binary_str[-5]=='1':
        result.reverse()
        return result
    print(result)
    return result
    
