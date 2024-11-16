import re
def CodelandUsernameValidation(str):
    if len(str) < 4 or len(str) > 25:
        return False
    if not str[0].isalpha():
        return False
    
    if not re.match(r'^[a-zA-z0-9_]+$', str):
        return False
    
    if str[-1] == '_':
        return False
    return True

print(CodelandUsernameValidation('__abc09'))
print(CodelandUsernameValidation(''))
print(CodelandUsernameValidation('abc__09'))
print(CodelandUsernameValidation('abc__'))
print(CodelandUsernameValidation('abc1'))