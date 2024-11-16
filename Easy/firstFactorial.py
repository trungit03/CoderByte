def firstFactorial(num):
    if num < 1 or num > 18:
        return 0
    
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(firstFactorial(8))