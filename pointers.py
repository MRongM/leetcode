class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def desc_make():
    head = Node(0)
    this = head

    for i in range(1, 10):
        this = Node(i, this)
    return this


def asc_make():
    head = Node(0)
    this = head

    for i in range(1, 10):
        next = Node(i)
        this.next = next
        this = next

    return head


def trav(this):
    while True:
        if this is None:
            break
        print(this.value)
        this = this.next


def make_circle(this):
    that = this
    for i in range(10):
        that = that.next
        if i == 5:
            break

    while True:
        if this.next is None:
            break
        this = this.next
    this.next = that


def check_circle(this):
    fast = slow = this

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            # slow.next = None
            return True
    return False


def get_circle(this):
    fast = slow = this

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break

    slow = this
    while slow is not fast:
        fast = fast.next
        slow = slow.next
    return slow


def find_last_k(this, k=5):
    fast = slow = this
    for _ in range(5):
        fast = fast.next
    while fast is not None:
        fast = fast.next
        slow = slow.next
    return slow.value


def binary_search(arr, value):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            high = mid - 1
        else:
            low = mid + 1


def twoSum(arr, value):
    low = 0
    high = len(arr) - 1
    while low < high:
        r = value - arr[low]
        if arr[high] == r:
            return low + 1, high + 1
        elif arr[high] > r:
            high -= 1
        else:
            low += 1


def reverse_list(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
    return arr


c = [2, 7, 11, 15, 18]
k = twoSum(c, 34)
print(k)
# c = range(11,100)
# cc = reverse_list(list(c))
# print(cc)
# idx = binary_search(list(c),99)
# print(idx)
#
# a = asc_make()
# print(check_circle(a))
# # make_circle(a)
# print()
# # check_circle(a)
# # trav(a)
# # c = get_circle(this=a)
# v = find_last_k(a)
# print(v)
