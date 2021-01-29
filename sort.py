def maxDistance(nums):
    """
    给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
    如果数组元素个数小于 2，则返回 0。
    请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
    """


def quickSort(nums):
    """
    快速排序
    :param nums:
    :return:
    """


def convertToTile(n):
    """
    给定一个正整数，返回它在 Excel 表中相对应的列名称。
    :param n:
    :return:
    """


def countZero(n):
    """
    给定一个整数 n，返回 n! 结果尾数中零的数量。
    :param n:
    :return:
    """


def largestNum(nums):
    nums_str = []

    for i in nums:
        nums_str.append(str(i))
    nums_str.sort(reverse=True)
    return ''.join(nums_str)


def mostPointsLine(points):
    """
    给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
    :param points:
    :return:
    """


nums = [1, 2, 3, 1, 3, 5, 1, 4, 5, 7]
res = largestNum(nums)
print(res)
