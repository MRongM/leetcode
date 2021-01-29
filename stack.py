class MinStack:
    """
    定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
    调用 min、push 及 pop 的时间复杂度都是 O(1)。
    """
    def __init__(self):
        self.stack = []
        self.min = []

    def pop(self):
        pass

    def push(self, x):
        pass

    def min(self):
        pass


def is_pop_order(nums1, nums2):
    """
    输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺
    序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列
    {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹
    出序列。
    :return:
    """