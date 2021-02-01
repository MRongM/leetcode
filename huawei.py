"""
import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))

"""


def hex2ten(nums):
    k = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    res = []
    for i in nums:
        i = i[2:]
        r = 0
        for j in i:
            n = k.get(j)
            if n is None:
                n = int(j)
            r = r * 16 + n
        else:
            res.append(r)
    return res


import math


def is_prime(x):
    res = True
    if x == 2:
        return res
    bound = int(math.sqrt(x)) + 2
    for i in range(2, bound):
        if x % i == 0:
            return False
    return True


def get_primes():
    n = int(input())
    if n < 2:
        return ' '

    while n % 2 == 0:
        print(2, end=" ")
        n = n // 2

    for i in range(3, n + 1, 2):

        while n % i == 0:
            print(i, end=" ")
            n = n // i


def get_primes2():
    a = int(input())
    i = 2
    n = a
    while i * i <= a and n > i:
        while n % i == 0:
            print(i, end=" ")
            n = n / 2
        n += 2


import threading


def writer(index, word, nums):
    for i in index:
        nums[i] = word


def abcdThread():
    ww = []
    n = 4 * 10
    nums = ['' for i in range(n)]
    words = ['A', 'B', 'C', 'D']
    for i in range(4):
        index = range(i, n, 4)
        t = threading.Thread(target=writer, args=(index, words[i], nums))
        ww.append(t)

    for t in ww:
        t.start()
        t.join()
    print(''.join(nums))


def binary_search(nums, target):
    l = 0
    r = len(nums) - 1
    mid = None
    while l <= r:
        mid = (l + r) // 2
        tmp = nums[mid] * nums[mid] * nums[mid]
        if tmp - target == 0.0:
            return mid
        elif tmp < target:
            l = mid + 1
        else:
            r = mid - 1
    if mid is not None:
        a1 = abs(multi3(nums[mid - 1]) - target)
        a2 = abs(multi3(nums[mid]) - target)
        a3 = abs(multi3(nums[mid + 1]) - target)
        if a1 <= a2:
            if a1 <= a3:
                return mid - 1
            else:
                return mid + 1
        else:
            if a2 <= a3:
                return mid
            else:
                return mid + 1

    return l


def binary_search2(target):
    l = 0
    r = target
    while r - l >= 0.00001:
        mid = (l + r) / 2
        tmp = multi3(mid)
        if tmp - target == 0.0:
            return mid
        elif tmp < target:
            l = mid + 0.1
        else:
            r = mid - 0.1
    return l


def generate_float_list(s, e):
    res = []
    it = float(s)
    for i in range(0, (e - s) * 10):
        res.append(round(it, 1))
        it += 0.1

    return res


def findEle(n):
    if n == 0:
        return 0.0

    if n < 0:
        x = -n
    else:
        x = n

    if x >= 1:
        nums = generate_float_list(1, int(x // 2))
    else:
        nums = generate_float_list(0, 1)

    idx = binary_search(nums, x)
    return nums[idx] if n > 0 else -nums[idx]


def multi3(n):
    return n * n * n


def newton(n):
    x = 1
    while abs(x * x * x - n) > 0.001:
        x = x - (x * x * x - n) / (3 * x * x)
    return round(x, 1)


def redraiment(nums):
    return res


import sys

# sys.stdin
for line in ['Jkdi234klowe90a3']:
    pre = None
    line = line.strip()
    res = []
    for i in range(len(line)):

        if line[i].isdigit():
            if pre is None or pre == 2:
                res.append('*')
            pre = 1

        if line[i].isalpha():
            if pre == 1:
                res.append("*")
            pre = 2
        res.append(line[i])

    else:
        if line[-1].isdigit():
            res.append("*")

    print(''.join(i for i in res))


def weight(s):
    po = {'3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12, '2': 13,
          'joker': 14, 'JOKER': 15}
    if len(s) == 1:
        return 1, po[s[0]]

    if len(s) == 2:
        if 'joker' in s:
            return 10, 1000
        return 2, 2 * po[s[0]]

    if len(s) == 3:
        return 3, 3 * po[s[0]]

    if len(s) == 4:
        return 10, 4 * po[s[0]]

    if len(s) == 5:
        return 5, po[s[0]]


def poker(ss):
    s0, s1 = ss.split('-')
    t0, w0 = weight(s0)
    t1, w1 = weight(s1)
    if t0 == t1:
        return s0 if w0 > w1 else s1

    if 10 == t0 or 10 == t1:
        return s0 if t0 == 10 else s1
    else:
        return 'ERROR'


po = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', 'joker', 'JOKER']
pp = {}
idx = 1
for i in po:
    pp[i] = idx
    idx += 1
print(pp)

a = [(1, 3), (2, 4), (3, 7)]
cc = sorted(a, key=lambda x: x[1], reverse=True)
print(cc)
# nums = [3,2,1]
# nums = [2,5,1,5,4,5]
# nums = [243, 277, 172, 222, 127, 70, 34, 1, 261, 277, 10, 151, 29, 159, 318, 16, 50, 41, 309, 315, 303, 47, 5, 257, 246,
#         32, 105, 96, 199, 304, 194, 7, 218, 158, 239, 244, 58, 9, 250, 326, 210, 194, 312, 281, 244, 79, 170, 316, 64,
#         291, 139, 178, 35, 299, 322, 21, 238, 54, 102, 105, 75, 17, 187, 55, 290, 115, 165, 51, 155, 107, 136, 112, 270,
#         164, 15, 26, 142, 158, 312, 31, 165, 262, 214, 1, 67, 213, 88, 283, 198, 95, 37, 317, 43, 301, 269, 25, 228,
#         321]
# res = redraiment(nums)
# print(res)
# 6
# 2 5 1 5 4 5
# 3
# 3 2 1

# print(newton(216))
# print(binary_search2(216))
# print(multi3(2.3))

# a = float(input())
# r = findEle(a)
# print(r)
#
# print(generate_float_list(1, 3))
# nums = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
# target = 3
# r = binary_search(nums, target)
# print(r, nums[r], nums[r - 1], nums[r + 1])
# print(target, multi3(nums[r]), multi3(nums[r - 1]), multi3(nums[r + 1]))

# a = ["cap","to","cat","card","two","too","up","boat","boot"]
# b = sorted(a)
# print(b)
# nums = ['0xAAA', '0xA', '0xA9A']
# rr = hex2ten(nums)
# print(rr)
# nums = list(range(2,100))
# res = []
# for i in nums:
#     if is_prime(i):
#         res.append(i)
# print(res)
# print(is_prime(64577))
# c = get_primes(280000000000000)
# print(c)
