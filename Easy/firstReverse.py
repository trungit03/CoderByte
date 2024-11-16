def firstReverse(strArray):
    result = ""
    for i in range(len(strArray) - 1, -1, -1):
        result += strArray[i]
    return result
#   return strArray[::-1]


print(firstReverse('Hello world'))