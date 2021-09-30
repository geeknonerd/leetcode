"""
101. 对称二叉树
树 深度优先搜索 广度优先搜索 二叉树
简单


给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
 

进阶：

你可以运用递归和迭代两种方法解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symmetric(left_n: TreeNode, right_n: TreeNode) -> bool:
            if not (left_n and right_n):
                return left_n == right_n
            if left_n.val != right_n.val:
                return False
            return symmetric(left_n.left, right_n.right) and symmetric(left_n.right, right_n.left)

        return symmetric(root.left, root.right)


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(1,
                 left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                 right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)))
    result = solution.isSymmetric(n)
    print(result)
    assert result is True

    n = TreeNode(1,
                 left=TreeNode(2, right=TreeNode(3)),
                 right=TreeNode(2, right=TreeNode(3)))
    result = solution.isSymmetric(n)
    print(result)
    assert result is False

