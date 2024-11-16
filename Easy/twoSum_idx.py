def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

nums = list(map(int, input().split()))
target_input = int(input())


result = twoSum(nums, target_input)
print(result)