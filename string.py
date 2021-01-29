def str_combination(s):
    """
    https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/
    输入一个字符串，打印出该字符串中字符的所有排列。
    你可以以任意顺序返回这个字符串数组，但里面不能有重复元素
    """


def longestSubStr(s):
    """

    :param s:
    :return:
    """
    n = len(s)


def firstUniqChar(s):
    res = {}
    for i in s:
        if res.get(i):
            res[i]+=1
        else:
            res[i] =1

    for i in s:
        if res.get(i) == 1:
            return i

    return " "