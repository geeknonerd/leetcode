"""
617. 合并二叉树
树 深度优先搜索 广度优先搜索
简单


给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-binary-trees
"""


# Definition for a binary tree node.
from typing import List, Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return '({})[{}, {}]'.format(self.val, self.left, self.right)


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 or not root2:
            return root2 if not root1 else root1
        return self.dfs(root1, root2)

    def dfs(self, r1: TreeNode, r2: TreeNode) -> TreeNode:
        if not r1 or not r2:
            return r2 if not r1 else r1
        r1.val += r2.val
        r1.left = self.dfs(r1.left, r2.left)
        r1.right = self.dfs(r1.right, r2.right)
        return r1


if __name__ == '__main__':
    solution = Solution()

    tree1 = TreeNode(1, left=TreeNode(3, left=TreeNode(5)), right=TreeNode(2))
    tree2 = TreeNode(2, left=TreeNode(1, right=TreeNode(4)), right=TreeNode(3, right=TreeNode(7)))
    print(tree1)
    print(tree2)
    result = solution.mergeTrees(tree1, tree2)
    print(result)
    assert str(result) == str(TreeNode(3,
                                       left=TreeNode(4, left=TreeNode(5), right=TreeNode(4)),
                                       right=TreeNode(5, right=TreeNode(7))))
