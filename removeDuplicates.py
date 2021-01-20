def removeDuplicates(nums):
    n = len(nums)
    if n <= 1:
        return n
    first = 0
    first_value = nums[first]

    for second in range(1, n):
        if first_value == nums[second]:
            continue
        else:
            first_value = nums[second]
            nums[first + 1] = nums[second]
            first += 1
    return first + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [1, 1, 2]
# nums = [0]*10
res = removeDuplicates(nums)
print(nums)
print(res)

