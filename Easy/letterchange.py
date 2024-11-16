def LetterChange(str):
    newstring = ""
    for char in str:
        if char.isalpha():
            if char.lower() == 'z':
                char = 'a'
            else:
                char = chr(ord(char) + 1)
            if char in 'aeiou':
                char = char.upper()
            newstring  = newstring + char
        else:
            newstring += char
    return newstring

print(LetterChange('zadb'))
print(LetterChange('zzaadb'))