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
    mins = []
    maxs = []
    n = len(nums)

    for i in range(n):
        if i == 0:
            maxs.append(nums[i])
            mins.append(nums[i])

        # if nums[i]>0:

