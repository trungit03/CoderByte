def BracketMatcher(str):
    stack = []
    for char in str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 0
            stack.pop()
    return 1 if not stack else 0

print(BracketMatcher('(coder), (youtube)'))
print(BracketMatcher('(coder), (youtube))'))
print(BracketMatcher('((coder), (youtube)'))