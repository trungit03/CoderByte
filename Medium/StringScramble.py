def StringScramble(str1, str2):
    s1 = list(str1)
    s2 = list(str2)

    i = 0
    while i < len(s1):
        j = 0
        while j < len(s2):
            if s1[i] == s2[j]:
                s1.pop(i)
                s2.pop(j)
                i -= 1
                break
            j+= 1
        i+=1
    if len(s2) == 0:
        return 'true'
    else:
        return 'false'
    

print(StringScramble('dwfavosalasrvsa', 'world'))
print(StringScramble('hello', 'hey'))