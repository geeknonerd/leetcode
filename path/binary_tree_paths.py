"""
257. 二叉树的所有路径
树 深度优先搜索 字符串 回溯 二叉树
简单


给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

叶子节点 是指没有子节点的节点。

 
示例 1：


输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]
示例 2：

输入：root = [1]
输出：["1"]
 

提示：

树中节点的数目在范围 [1, 100] 内
-100 <= Node.val <= 100

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-tree-paths
"""
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = deque()
        ret = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            stack.append(node.val)
            if node.left is None and node.right is None:
                ret.append('->'.join(map(lambda x: str(x), stack)))
                stack.pop()
                return
            dfs(node.left)
            dfs(node.right)
            stack.pop()

        dfs(root)
        return ret


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(1, left=TreeNode(2, right=TreeNode(5)), right=TreeNode(3))
    result = solution.binaryTreePaths(n)
    print(result)
    assert result == ["1->2->5", "1->3"]

    n = TreeNode(1)
    result = solution.binaryTreePaths(n)
    print(result)
    assert result == ["1"]
