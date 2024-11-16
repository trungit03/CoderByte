def firstIntersection(strArray):
    list1 = list(map(int, strArray[0].strip().split(',')))
    list2 = list(map(int, strArray[1].strip().split(',')))
    intersection = []
    for x in list1:
        if x in list2:
            intersection.append(x)
            list2.remove(x)
    
    if not intersection:
        return False
    return ','.join(map(str, intersection))

print(firstIntersection(["1, 2, 3, 4, 5", "7, 1, 3, 9"]))