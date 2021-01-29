def binaryD(n):
    return n > 0 and n & (n - 1) == 0


def findOne(n):
    """
    请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二
    进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。
    :param n:
    :return:
    """
    res = 0

    while n != 0:
        n &= n - 1
        res += 1
    return res


r = findOne(9)
print(r)
