"""
102. 二叉树的层序遍历
树 广度优先搜索 二叉树
中等


给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
"""
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        res = []
        queue.append(root)
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                node = queue.popleft()
                if not node:
                    continue
                tmp.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if tmp:
                res.append(tmp)
        return res


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    result = solution.levelOrder(n)
    print(result)
    assert result == [[3], [9, 20], [15, 7]]
