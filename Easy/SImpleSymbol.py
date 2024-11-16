def SimpleSymbol(str):
    if str[0].isalpha():
        return 'false'
    if str[-1].isalpha():
        return 'false'
    for i in range(1, len(str) - 1):
        if str[i].isalpha():
            if str[i-1] != '+' or str[i+1] != '+':
                return 'false'
    return 'true'
print(SimpleSymbol('++d+===+c++==+a=='))