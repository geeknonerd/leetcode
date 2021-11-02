"""
230. 二叉搜索树中第K小的元素
树 深度优先搜索 二叉搜索树 二叉树
中等


给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

 

示例 1：


输入：root = [3,1,4,null,2], k = 1
输出：1
示例 2：


输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
 

 

提示：

树中的节点数为 n 。
1 <= k <= n <= 10^4
0 <= Node.val <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


if __name__ == '__main__':
    solution = Solution()

    tree = TreeNode(3, left=TreeNode(1, right=TreeNode(2)),
                    right=TreeNode(4))
    result = solution.kthSmallest(tree, 1)
    print(result)
    assert result == 1

    tree = TreeNode(5, left=TreeNode(3, left=TreeNode(2, left=TreeNode(1)),
                                     right=TreeNode(4)),
                    right=TreeNode(6))
    result = solution.kthSmallest(tree, 3)
    print(result)
    assert result == 3
