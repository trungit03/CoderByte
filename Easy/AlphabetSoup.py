def AlphabetSoup(str):
    char = list(str)
    char.sort()
    return ','.join(char)

print(AlphabetSoup('codelearn'))