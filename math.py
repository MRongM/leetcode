def fibonacci(n):
    """
    斐波那契数列
    :param n:
    :return:
    """
    if n == 0:
        return 0

    if n <= 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci2(n):
    if n == 0:
        return 0

    pre = 0
    cur = 1
    for i in range(n):
        cur += pre
        pre = cur
    return cur


def cutRope(n):
    dp = [0 for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(i):
            print(dp[i], (i - j) * j, j * dp[i - j], j, i, dp)
            dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))

    print(dp)
    return dp[n]


def cuttingRope(n):
    if n == 1:
        return 1

    if n == 2:
        return 2
    ans = 1

    while n > 4:
        ans *= 3
        n -= 3
        ans %= 1000000007
    print(ans)
    ans *= n
    return ans % 1000000007


def print_n(n):
    res = ''.join(['9'] * n)
    for i in range(1, int(res) + 1):
        print(i, end=' ')


def isNumber(s):
    """
    请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、
    "5e2"、"-123"、"3.1416"、"0123"及"-1E-16"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"
    及"12e+5.4"都不是
    :param s:
    :return:
    """
    s = s.strip()
    s = s.lower()
    flag = False
    for i in s:
        pass


def isUgly(num):
    if num == 1:
        return True
    if num < 0:
        return False

    a = [2, 3, 5]
    for i in a:
        while num % i == 0:
            num = num / i
            if num == 1:
                return True
    return False


# for i in range(2, 20):
#     print(i, ' ', isUgly(i))
#
# c = -2147483648
# print(c, ' ', isUgly(c))
# r1 = []
# r2 = []
# for i in range(10):
#     r = fibonacci(i)
#     r1.append(r)
#
# for i in range(10):
#     r = fibonacci(i)
#     r2.append(r)
#
# print(r1)
# print(r2)
# r = cutRope(9)
# r = cuttingRope(8)
# print(r)
# print_n(2)

def romanToInt(s):
    o={
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    if len(s) == 1:
        return o.get(s)

    ans = 0
    pre = o.get(s[0])
    for i in s[1:]:
        cur = o.get(i)
        if cur>pre:
            ans+=cur-pre-pre
        else:
            ans+=cur
        pre = cur

    return ans

