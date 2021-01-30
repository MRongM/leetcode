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


def writer(index,word,nums):
    for i in index:
        nums[i] = word


ww = []
n = 4*10
nums = ['' for i in range(n)]
words = ['A','B','C','D']
for i in range(4):
    index = range(i, n, 4)
    t = threading.Thread(target=writer,args=(index, words[i],nums))
    ww.append(t)

for t in ww:
    t.start()
    t.join()
print(''.join(nums))
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
