def ArrayMatching(strArray):
    a = eval(strArray[0])
    b = eval(strArray[1])

    result = []
    for i in range(min(len(a), len(b))):
        result.append(a[i] + b[i])

    if len(a) > len(b):
        result.extend(a[len(b):])
    elif len(b) > len(a):
        result.extend(b[len(a):])
    
    return '-'.join(map(str, result))
print(ArrayMatching(['[1, 2]', '[1, 2, 3]']))