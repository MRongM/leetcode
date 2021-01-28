res = []
item = []


def combinationSum(nums, target):
    def backtrace(nums, res, sum_, index):
        if sum_ > target:
            return

        if sum_ == target:
            res.append(item)
            return

        for i in range(index, len(nums)):
            su = sum_ + nums[i]
            item.append(nums[i])
            backtrace(nums, item, su, i)
            item.pop(-1)

    backtrace(nums, res, 0, 0)


def combination(n, k):
    def backtrace(n, k, index, tmp):

        if tmp == k:
            res.append(''.join([str(i) for i in item]))
            return

        for i in range(index, n + 1):
            item.append(i)
            backtrace(n, k, i + 1, tmp + 1)
            item.pop(-1)

    backtrace(n, k, 1, 0)


# nums = [1, 2, 4, 8, 5, 3, 12, 1, 23, 3, 4, 2, 1, 1, 6, 3, 2, 2]
# combinationSum(nums, 3)
combination(4, 3)
print(res)
