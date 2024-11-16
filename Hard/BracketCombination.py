def BracketCombination(num):
    def generate_combination(open_count, close_count):
        nonlocal count 
        if open_count == num and close_count == num:
            count += 1
            return
        if open_count < num:
            generate_combination(open_count +1, close_count)
        if close_count < open_count:
            generate_combination(open_count, close_count + 1)
    count = 0
    generate_combination(0, 0)
    return count

print(BracketCombination(2))