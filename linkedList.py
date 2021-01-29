class Node:
    def __init__(self, val, nnext=None):
        self.val = val
        self.next = nnext


def mergeList(p1, p2):
    head = res = None
    while p1 and p2:
        if p1.val > p2.val:
            tmp = Node(p2.val)
            p2 = p2.next
        else:
            tmp = Node(p1.val)
            p1 = p1.next

        if res:
            res.next = tmp
            res = res.next
        else:
            head = res = tmp

    if p1:
        res.next = p1

    if p2:
        res.next = p2
    return head


def make_list(arr):
    head1 = lis1 = None

    for i in arr:
        tmp = Node(i)
        if lis1:
            lis1.next = tmp
            lis1 = lis1.next
        else:
            head1 = lis1 = tmp

    return head1


def print_lis(arr):
    rr = []
    while arr:
        rr.append(arr.val)
        arr = arr.next
    print(','.join(str(r) for r in rr))


from otils import cost


@cost()
def mergeMultiList(arr_link):
    # 循环n次
    n = len(arr_link)

    first = arr_link[0]
    for i in range(1, n):
        first = mergeList(first, arr_link[i])

    return first


@cost()
def mergeMultiList2(arr_link, start, end):
    if end - start == 0:
        return arr_link[start]

    if end - start == 1:
        return mergeList(arr_link[start], arr_link[end])

    mid = (start + end) // 2

    return mergeList(mergeMultiList2(arr_link, start, mid), mergeMultiList2(arr_link, mid + 1, end))


def insert(cur, node):
    head0 = cur
    pre = None

    while cur:
        if cur.val > node.val:
            break
        pre = cur
        cur = cur.next

    if not cur:
        pre.next = node
    else:
        if pre:
            node.next = cur
            pre.next = node
        else:
            node.next = head0
            head0 = node
    return head0


def sort_list(arr):
    pre, cur = Node(arr.val), arr.next
    while cur:
        pre = insert(pre, Node(cur.val))
        cur = cur.next

    return pre


def find_mid(head):
    pre = cur = head
    while cur and cur.next:
        cur = cur.next.next
        pre = pre.next
    return pre


def twoNode(node1, node2):
    if node1 and node2:
        if node1.val < node2.val:
            node1.next = node2
            return node1
        else:
            node2.next = node1
            return node2

    return node1 if node1 else node2


def sort_list2(arr):
    # 归并排序链表
    if not arr or not arr.next:
        return arr
    pre, cur = arr, arr.next

    while cur and cur.next:
        pre = pre.next
        cur = cur.next.next

    right = pre.next
    pre.next = None
    left = arr
    left = sort_list2(left)
    right = sort_list2(right)

    res = head = Node(-1)

    while left and right:
        if left.val < right.val:
            head.next = left
            left = left.next
        else:
            head.next = right
            right = right.next
        head = head.next

    head.next = left if left else right
    return res.next


def addTwoNumber(lis1, lis2):
    # https://leetcode-cn.com/problems/add-two-numbers/submissions/
    a1 = []
    a2 = []
    while lis1:
        a1.append(lis1.val)
        lis1 = lis1.next

    while lis2:
        a2.append(lis2.val)
        lis2 = lis2.next

    res = []
    s = 0
    while a1 or a2:
        x = a1.pop(-1) if a1 else 0
        y = a2.pop(-1) if a2 else 0
        k = x + y + s
        if k > 9:
            k = k%10
            s = 1
        else:
            s = 0

        res.insert(0, k)

    if s:
        res.insert(0, s)
    return res


def reverse_list(arr):

    pre = None
    cur = arr
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre


def reverse_link(link):
    if not link or not link.next:
        return link
    print_lis(link)
    print("="*10)
    cur = reverse_link(link.next)
    print_lis(link)
    print("*"*10)
    link.next.next = link
    link.next = None
    print_lis(link)
    print("&"*10)
    print_lis(cur)
    print("$"*10)

    return cur


def swapPair(head):
    if not head or not head.next:
        return head
    next = head.next
    head.next = swapPair(next.next)
    next.next = head
    return next


def swapPair2(head):
    if not head:
        return head
    cur = head
    pre = None
    while cur:
        cur.next = pre
        pre = cur
        cur = cur.next
    next = head.next
    head.next = swapPair(next.next)
    next.next = head
    return next


def deleteNode(head, node):
    pre = head
    if not head.next:
        return pre
    hnext = head.next
    while hnext:
        if hnext.val == node.val:
            head.next = hnext.next
        head = head.next
        hnext = hnext.next
    return pre


def oodFirst(head):
    """
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前
    半部分，所有偶数位于数组的后半部分
    :param head:
    :return:
    """


def copyRandomList(head):
    """
    https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/
    请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个
    next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
    :return:
    """


def tree2list(root):
    """
    https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
    输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何
    新的节点，只能调整树中节点指针的指向。
    :param root:
    :return:
    """


head1 = make_list([5,3])
head2 = make_list(range(2, 9, 2))
head3 = make_list(range(10, 900, 3))
head4 = make_list(range(30, 1000, 4))
# new_lis = mergeList(head1, head2)
# print_lis(new_lis)
# oo = [head1 for _ in range(100)]
# mergeMultiList(oo)
# new_lis = mergeMultiList2(oo, 0, len(oo) - 1)
# print_lis(new_lis)
# cc = find_mid(head1)
# print(cc.val)

# inode = insert(head1,Node(0))
# print_lis(inode)
# inode = insert(head1,Node(1))
# print_lis(inode)
# inode = insert(head1,Node(5))
# print_lis(inode)
# inode = insert(head1,Node(55))
# print_lis(inode)
# import random
#
# cc = list(range(1, 22, 2))
# random.shuffle(cc)
# head9 = make_list(cc)
# print_lis(head9)
# mm = sort_list2(head9)
# print_lis(mm)

# res = addTwoNumber(head1, head2)
print_lis(head1)
print_lis(head2)
# cc = reverse_list(head2)
# cc = reverse_link(head2)
# cc = swapPair(head2)
# print_lis(cc)
# print(res)
print_lis(head2)
cc = deleteNode(head2,Node(8))
print_lis(cc)