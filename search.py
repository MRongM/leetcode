def search(nums, target):
    low = 0
    high = len(nums) - 1
    finder = None

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            finder = mid
            break
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if finder is not None:
        counter = 1
        for i in range(finder + 1, len(nums)):
            if nums[i] == target:
                counter += 1
            else:
                break

        for i in range(finder - 1, -1, -1):
            if nums[i] == target:
                counter += 1
            else:
                break

        return counter
    return 0


nums = [5, 7, 7, 8, 8, 10]
cc = search(nums, target=8)
print(cc)
