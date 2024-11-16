def StringReduction (string):
    string_reductions = {
        'ac': 'b',
        'ca': 'b',
        'bc': 'a',
        'ab': 'c',
        'cb':'a'
    }

    string_reduction = ""
    flag = False
    i = 0
    while i < len(string):
        if i < len(string) - 1:
            substring = string[i] + string[i+1]
            if substring in string_reductions:
                flag = True
                string_reduction += string_reductions[substring]
                i+=2
            else:
                string_reduction += string[i]
                i += 1
        else:
            string_reduction += string[i]
            i += 1
    if flag:
        return StringReduction(string_reduction)
    else:
        return len(string_reduction)
    

print(StringReduction('cab'))