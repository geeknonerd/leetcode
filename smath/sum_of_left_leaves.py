"""
404. 左叶子之和
树 深度优先搜索 广度优先搜索 二叉树
简单


给定二叉树的根节点 root ，返回所有左叶子之和。

 

示例 1：



输入: root = [3,9,20,null,null,15,7]
输出: 24
解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
示例 2:

输入: root = [1]
输出: 0
 

提示:

节点数在 [1, 1000] 范围内
-1000 <= Node.val <= 1000


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sum-of-left-leaves
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum_node = 0

        def recursion(is_left: bool, node: Optional[TreeNode]):
            nonlocal sum_node
            if not node:
                return
            if is_left and not node.left and not node.right:
                sum_node += node.val
                return
            recursion(True, node.left)
            recursion(False, node.right)

        recursion(False, root)
        return sum_node


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    result = solution.sumOfLeftLeaves(n)
    print(result)
    assert result == 24

    n = TreeNode(1)
    result = solution.sumOfLeftLeaves(n)
    print(result)
    assert result == 0
