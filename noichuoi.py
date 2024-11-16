def noichuoi(str1, str2):

    result = []
    max_length= max(len(str1), len(str2))
    for i in range(max_length):
        if i < len(str1):
            result.append(str1[i])
        if i < len(str2):
            result.append(str2[i])

    return ''.join(result)
print(noichuoi('abcd', 'world'))