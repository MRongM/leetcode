# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def make_tree(arr):
    def _make_tree(node, v):
        tmp = TreeNode(v)
        if node.val >= v:
            node.left = tmp
        else:
            node.right = tmp

    n = len(arr)
    root = node = None
    for i in range(n):
        tmp = TreeNode(arr[i])
        if node:
            if node.val >= arr[i]:
                node.left = tmp
            else:
                node.right = tmp
        if i == 0:
            root = tmp
        else:
            node = tmp

    return root


def convertBiNode(root):
    if not root:
        return root
    left = root.left
    root.left = convertBiNode(root.right)
    root.right = convertBiNode(left)
    return root


def trav_tree(root, order=1):
    res = []
    if root is None:
        return res
    if order == 1:
        res.append(root.val)
    res.extend(trav_tree(root.left, order))
    if order == 2:
        res.append(root.val)
    res.extend(trav_tree(root.right, order))
    if order == 3:
        res.append(root.val)
    return res


def traversal_layer(nodes):
    res = []
    if not nodes:
        return res

    nexts = []
    for no in nodes:
        res.append(no.val)
        if no.left:
            nexts.append(no.left)
        if no.right:
            nexts.append(no.right)
    ss = traversal_layer(nexts)
    res.extend(ss)
    return res
    # return res.extend(ss)


def bad_way():
    r = TreeNode(4)
    n2 = TreeNode(2)
    n3 = TreeNode(5)
    r.left = n2
    r.right = n3

    n4 = TreeNode(1)
    n5 = TreeNode(3)
    n2.left = n4
    n2.right = n5
    n3.left = TreeNode('null')
    n3.right = TreeNode(6)

    n4.left = TreeNode(0)
    return r


po = []


def inorder(root):
    if not root:
        return
    left = root.left
    inorder(left)
    root.left = None
    print(root.val)
    inorder(root.right)


r = bad_way()
# t1 = trav_tree(r)
# t2 = trav_tree(r, 2)
# t3 = trav_tree(r, 3)
# t4 = traversal_layer([r])
# inorder(r)
rr = convertBiNode(r)
# inorder(r)
#
