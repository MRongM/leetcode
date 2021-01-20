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



so = Solution()
nums = [-1, 0, 1, 2, -1, -4]
res = so.threeSum(nums)
print(res)
