def minPathSum(grid):
    """
    https://leetcode-cn.com/problems/minimum-path-sum/
    :return:
    """
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            tp = 1e9
            if i > 0:
                tp = min(tp, grid[i - 1][j])
            if j > 0:
                tp = min(tp, grid[i][j - 1])
            grid[i][j] += tp

    return grid[-1][-1]


def maxProduct(nums):
    """
    https://leetcode-cn.com/problems/maximum-product-subarray/
    :return:
    """
    n = len(nums)
    ans = 0
    max_ = min_ = nums[0]
    for i in range(1, n):
        mx, mn = max_, min_
        max_ = max(mx * nums[i], nums[i], mn * nums[i])
        min_ = min(mx * nums[i], nums[i], mn * nums[i])
        ans = max(max_, ans)
    return ans


def maxSubArray(nums) -> int:
    """
    https://leetcode-cn.com/problems/maximum-subarray/
    :param nums:
    :return:
    """
    n = len(nums)
    matrix = [0 for i in range(n)]
    ans = matrix[0] = nums[0]
    for j in range(1, n):
        matrix[j] = max(matrix[j - 1] + nums[j], nums[j])
        print(matrix)
    return max(matrix)


def compare(a, b):
    m, n = len(a), len(b)
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        pre = dp[::]
        dp[0] = i
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[j] = pre[j - 1]
            else:
                dp[j] = min(pre[j], pre[j - 1], dp[j - 1]) + 1
            print(dp, pre)
    return dp[-1]


def massage(nums):
    """
    https://leetcode-cn.com/problems/the-masseuse-lcci/
    :param nums:
    :return:
    """
    # [1, 2, 3, 1]
    dp = []
    for i in range(len(nums)):
        dp.append(nums[i])
        for j in range(i):
            if i - j != 1:
                dp[j] = max(dp[j], dp[j - 1] + nums[j])
                print(dp, i)
    return max(dp)


def divisorGame(n):
    """
    https://leetcode-cn.com/problems/divisor-game/
    :param n:
    :return:
    """
    return n % 2 == 0


def maxProfit(nums):
    """
    https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
    :param nums:
    :return:
    """
    # n = len(nums)
    # res = [0 for _ in range(n)]
    # pre = nums[0]
    # for i in range(1, n):
    #     pro = nums[i] - pre
    #     res[i] = max(pro, res[i - 1])
    #     if pro < 0:
    #         pre = nums[i]
    # return res[-1]

    n = len(nums)
    res = 0
    pre = nums[0]
    for i in range(1, n):
        pro = nums[i] - pre
        res = max(pro, res)
        if pro < 0:
            pre = nums[i]
    return res

# prices = [7,6,4,3,1]
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
# nums = [1, 2, 3, 1]
# nums = [2, 1, 4, 5, 3, 1, 1, 3]
# print(massage(nums))
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# maxSubArray(nums)
# a = 'abcdefg'
# b = 'abcddef'
# r = compare(a, b)
# print(r)
