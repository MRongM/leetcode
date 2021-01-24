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


def merge_sort_list(arr):
    pass

head1 = make_list(range(1, 23, 2))
head2 = make_list(range(2, 500, 2))
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
import random

cc = list(range(1, 1000, 2))
random.shuffle(cc)
head9 = make_list(cc)
print_lis(head9)
mm = sort_list(head9)
print_lis(mm)
