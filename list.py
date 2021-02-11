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
    cc = sorted(res.items(), key=lambda x: -x[1])
    return cc


def majorityElement4(nums):
    from collections import Counter
    cnt = Counter(nums)
    cc = cnt.most_common(1)
    return cc


def happyNum(num):
    str_num = str(num)
    sum_ = 0
    res = {}
    while sum_ != 1:
        sum_ = 0
        for i in str_num:
            k = int(i)
            sum_ += k * k
        if res.get(str_num):
            return False
        res[str_num] = sum_
        str_num = str(sum_)
    return True


def computeArea(A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
    if C <= E or B >= H or A >= G or F >= D:
        common_area = 0
    else:
        width = min(G, C) - max(A, E)
        height = min(H, D) - max(B, F)
        common_area = width * height
    area = (C - A) * (D - B) + (G - E) * (H - F) - common_area
    return area


def find_duplicate(nums):
    res = {i: False for i in nums}

    for i in nums:
        if res.get(i):
            return i
        else:
            res[i] = True
    return False


def isInMatrix(matrix, num):
    """
    在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上
    到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中
    是否含有该整数。
    注意点：首先判断矩阵是否为空，然后进行行遍历，首先判断是否需要遍历该行的每列元
    素，然后知道结束，中间找到元素则回 返回 true
    :param matrix:
    :param num:
    :return:
    """


def replaceSpace(words):
    """
    请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
    :param words:
    :return:
    """
    wlist = words.split(' ')
    return "%20".join(wlist)


def find_half(nums):
    # nums.sort()
    res = {}
    n = len(nums) // 2
    for ix, i in enumerate(nums):
        if res.get(i):
            res[i] += 1
        else:
            res[i] = 1
        if res.get(i) > n:
            return i


def getLeastNumbers(nums, k):
    """
    https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
    :param nums:
    :param k:
    :return:
    """
    res = []

    for i in nums:
        if len(res) == k and res[k - 1] <= i:
            continue

        index = 0
        for ri in res:
            if ri >= i:
                break
            index += 1

        if len(res) == k:
            res.pop()
        res.insert(index, i)
    return res


def insert(r, value, k):
    index = 0
    for i in r:
        if i >= value:
            break
        index += 1

    if len(r) == k:
        r.pop()
    r.insert(index, value)


def getIntersectionNode(headA, headB):
    PA = headA
    PB = headB
    while PA != PB:
        if PA:
            PA = PA.next
        else:
            PA = headB

        if PB:
            PB = PB.next
        else:
            PB = headA
    return PA


def maxWidthOfVerticalArea(points):
    """
    https://leetcode-cn.com/problems/widest-vertical-area-between-two-points-containing-no-points
    :param points:
    :return:
    """
    res = []
    for i, _ in points:
        res.append(i)

    res = sorted(res)
    n = len(res)
    if n <= 1:
        return 0
    pre = 0
    cur = 1
    ans = []
    while cur < n:
        pre_value = res[pre]
        cur_value = res[cur]
        ans.append(cur_value - pre_value)
        pre += 1
        cur += 1
    return max(ans)


points = [[8, 7], [9, 9], [7, 4], [9, 7]]
r = maxWidthOfVerticalArea(points)
print(r)
#
# a = [3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
# print(find_half(a))
#
# a = [1, 2, 2, 2, 2, 1, 2, 3, 4, 5, 2, 1, 1, 1]
#
# # cnt, cand = majorityElement2(a)
# # res = majorityElement3(a)
# # res = majorityElement4(a)
# res = replaceSpace("my name  is xiaoming haha ")
# # happyNum(7)
# #
# print(res)
