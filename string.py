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
            res[i] += 1
        else:
            res[i] = 1

    for i in s:
        if res.get(i) == 1:
            return i

    return " "


def decompress(s):
    w = True
    res = []
    item = ''
    for i in s:
        if i.isdigit():
            if w:
                res.append([item, 0])
                item = ''
                w = False
            item += i
        else:
            if not w:
                res[-1][1] = int(item)
                item = ''
                w = True
            item += i
    else:
        if not w:
            res[-1][1] = int(item)

    def count(s):
        c = 0
        for i in s:
            c += ord(i)
        return c

    cc = sorted(sorted(res, key=lambda x: count(x[0])), key=lambda x: x[1])
    print(cc)
    r = ''
    for w, n in cc:
        r += w * n
    return r


def longestCommonSubsequence(text1, text2):
    # n = len(text1)
    # m = len(text2)
    # dp = dp1 = dp2 = dp3 = 0
    # for i in range(1, n + 1):
    #     for j in range(1, m + 1):
    #         if text1[i - 1] == text2[j - 1]:
    #             dp = dp3 + 1
    #             dp3 = dp
    #         else:
    #             dp1 = max(dp1,dp3)
    #             dp2 = max(dp2,dp3)
    #             dp = max(dp1,dp2)
    # return dp

    n = len(text1)
    m = len(text2)
    dp =[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            print(dp)
    return dp[-1][-1]

    # def dp(i, j):
    #     if i == -1 or j == -1:
    #         return 0
    #
    #     if text1[i] == text2[j]:
    #         return dp(i - 1, j - 1) + 1
    #     else:
    #         return max(dp(i - i, j), dp(i, j - 1))
    #
    # return dp(n - 1, m - 1)


a = "abcde"
b = "ace"
longestCommonSubsequence(b, a)
# s = 'a11b2bac3bad3abcd2'
# print(decompress(s))
