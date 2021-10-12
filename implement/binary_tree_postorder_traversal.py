"""
145. 二叉树的后序遍历
栈 树 深度优先搜索 二叉树
简单


给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(node: TreeNode):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

        res = []
        postorder(root)
        return res


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    result = solution.postorderTraversal(n)
    print(result)
    assert result == [3, 2, 1]
