"""
104. 二叉树的最大深度
树 深度优先搜索 广度优先搜索 二叉树
简单


给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(node: TreeNode) -> int:
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))
        return depth(root)


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    result = solution.maxDepth(n)
    print(result)
    assert result == 3
