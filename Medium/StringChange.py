def StringChange(str):
    result = ""
    i= 0
    while i < len(str):
        if str[i] == 'M':
            if i > 0:
                result += str[i-1]
            i+=1
        elif str[i] == 'N':
            i+=2
        else:
            result += str[i]
            i+=1
    return result    

print(StringChange('abcNdgM'))
print(StringChange('abcMdefNghi'))