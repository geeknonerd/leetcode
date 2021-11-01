"""
113. 路径总和 II
树 深度优先搜索 回溯 二叉树
中等


给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

 

示例 1：


输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
示例 2：


输入：root = [1,2,3], targetSum = 5
输出：[]
示例 3：

输入：root = [1,2], targetSum = 0
输出：[]
 

提示：

树中节点总数在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
"""
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node: TreeNode, val: int):
            if not node:
                return
            tmp.append(node.val)
            if not node.left and not node.right:
                if node.val == val:
                    res.append(list(tmp))
            else:
                if node.left:
                    dfs(node.left, val - node.val)
                if node.right:
                    dfs(node.right, val - node.val)
            tmp.pop()

        tmp = deque()
        res = []
        dfs(root, targetSum)
        return res


if __name__ == '__main__':
    solution = Solution()

    tree = TreeNode(5, left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))),
                    right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, left=TreeNode(5), right=TreeNode(1))))
    result = solution.pathSum(tree, 22)
    print(result)
    assert result == [[5, 4, 11, 2], [5, 8, 4, 5]]

    tree = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    result = solution.pathSum(tree, 5)
    print(result)
    assert result == []

    tree = TreeNode(1, left=TreeNode(2))
    result = solution.pathSum(tree, 0)
    print(result)
    assert result == []
