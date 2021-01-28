def majorityElement(nums):
    result = []

    if len(nums) == 0:
        return result

    count1 = count2 = candidate1 = candidate2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            count1 = 1
            candidate1 = num
        elif count2 == 0:
            count2 = 1
            candidate2 = num
        else:
            count1 -= 1
            count2 -= 1
    return result


def majorityElement2(nums):
    count1 = candidate1 = 0
    for num in nums:
        if count1 == 0:
            candidate1 = num
            count1 += 1
        else:
            if num == candidate1:
                count1 += 1
            else:
                count1 -= 1

    return count1, candidate1


def majorityElement3(nums):
    from collections import OrderedDict
    res = {}
    for num in nums:
        key = res.get(num)
        if key is not None:
            res[num] += 1
        else:
            res[num] = 1
    cc = sorted(res.items(),key=lambda x: -x[1])
    return cc


def majorityElement4(nums):
    from collections import Counter
    cnt = Counter(nums)
    cc = cnt.most_common(1)
    return cc



a = [1, 2, 2, 2, 2, 1, 2, 3, 4, 5, 2, 1, 1, 1]

# cnt, cand = majorityElement2(a)
# res = majorityElement3(a)
res = majorityElement4(a)
print(res)
