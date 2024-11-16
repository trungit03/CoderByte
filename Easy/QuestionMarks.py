def QuestionMarks(sen):
    # digits = []
    # for i, char in enumerate(str):
    #     if char.isdigit():
    #         digits.append((i, int(char)))
    
    # for i in range(len(digits)):
    #     for j in range(i+1, len(digits)):
    #         if digits[i][1] + digits[j][1] == 10:
    #             start = digits[i][0]
    #             end = digits[j][0]

    #             if end > start:
    #                 question_mark = str[start + 1: end].count('?')

    #                 if question_mark != 3:
    #                     return 'false'
    #                 else:
    #                     return 'true'
    # return 'false'
                
    lastdigits = None
    flag = False
    for i in range(len(sen)):
        if sen[i].isdigit():
            if lastdigits:
                if int(sen[i]) + int(sen[lastdigits]) == 10:
                    if sen[lastdigits:i].count('?') == 3:
                        flag = True
                    else: 
                        flag = False
            lastdigits = i
    
    return flag

print(QuestionMarks('abcs5?dasda?ko?5dad??dasda'))

print(QuestionMarks('abcd???10'))
print(QuestionMarks('abcd5???5dsa10'))