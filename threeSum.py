class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        res = []
        rm = []
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        rr = {nums[i], nums[j], nums[k]}
                        if rr not in rm:
                            rm.append(rr)
                            res.append([nums[i], nums[j], nums[k]])
                        break
        return res


def threeSum(nums):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n):
        first = nums[i]
        if i > 0 and first == nums[i - 1]:
            continue
        k = n - 1
        target = -first
        for j in range(i + 1, n):
            second = nums[j]
            if j > i + 1 and second == nums[j - 1]:
                continue

            third = nums[k]
            while j < k and third + second > target:
                k -= 1
                third = nums[k]
            if j == k:
                break
            if first + second + third == 0:
                res.append([first, second, third])
    return res


so = Solution()
nums = [-1, 0, 1, 2, -1, -4]
# res = so.threeSum(nums)
res = threeSum(nums)
print(res)
