class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    """
    https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/
    输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序
    遍历的结果中都不含重复的数字。
    """
    if not preorder:
        return None

    tree = TreeNode(preorder[0])
    loc = inorder.index(preorder[0])
    tree.left = buildTree(preorder[1:loc + 1], inorder[:loc])
    tree.right = buildTree(preorder[loc + 1:], inorder[loc + 1:])

    return tree


def treeHeight(root):
    if not root:
        return 0

    left = treeHeight(root.left)
    right = treeHeight(root.right)
    return max(left, right) + 1


def mergeTree(roota, rootb):
    """
    输入两棵二叉树 A 和 B，判断 B 是不是 A 的子结构。(约定空树不是任意一个树的子结构)
    B 是 A 的子结构， 即 A 中有出现和 B 相同的结构和节点值。
    :param root:
    :return:
    """


def mirrorTree(root):
    """
    请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那
    么它是对称的。
    :param root:
    :return:
    """


def order_traversal(root):
    """
    从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
    :param root:
    :return:
    """


def each_layer_traveral(root):
    """
    从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
    :param root:
    :return:
    """


def zhi_traveral(root):
    """
    请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按
    照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推
    :param root:
    :return:
    """


def post_traversal_check(root, nums):
    """
    https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
    输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true ，
    否则返回 false 。假设输入的数组的任意两个数字都互不相同。
    :param root:
    :param nums:
    :return:
    """


def traversal_path(root, value):
    """
    https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
    输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根
    节点开始往下一直到叶节点所经过的节点形成一条路径。
    :param root:
    :param value:
    :return:
    """
