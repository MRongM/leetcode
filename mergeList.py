class Node:
    def __init__(self, val, nnext=None):
        self.val = val
        self.next = nnext


def mergeList(p1, p2):
    head = res = None
    while p1 and p2:
        if p1.val>p2.val:
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


head1 = lis1 = None

for i in range(1,20,2):
    tmp = Node(i)
    if lis1:
        lis1.next = tmp
        lis1 = lis1.next
    else:
        head1 = lis1 = tmp

head2 = lis2 = None
for i in range(2, 30, 2):
    tmp = Node(i)
    if not lis2:
        head2 = lis2 = tmp
    else:
        lis2.next = tmp
        lis2 = lis2.next

# while head1:
#     print(head1.val)
#     head1 = head1.next
#
# while head2:
#     print(head2.val)
#     head2 = head2.next


new_lis = mergeList(head1, head2)

while new_lis:
    print(new_lis.val)
    new_lis = new_lis.next