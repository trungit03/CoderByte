def TwoSum(nums, target):
    num_map = {}
    pairs = []
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            pairs.append(f'{complement}, {num}')
        num_map[num] = True

    return ' '.join(pairs)
print(TwoSum([1, 2, 3, 4, 5], 6))