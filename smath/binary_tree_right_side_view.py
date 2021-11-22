"""
199. 二叉树的右视图
树 深度优先搜索 广度优先搜索 二叉树
中等


给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

 

示例 1:



输入: [1,2,3,null,5,null,4]
输出: [1,3,4]
示例 2:

输入: [1,null,3]
输出: [1,3]
示例 3:

输入: []
输出: []
 

提示:

二叉树的节点个数的范围是 [0,100]
-100 <= Node.val <= 100 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
"""
from collections import deque
from typing import List, Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        def bfs(node_queue: Deque[TreeNode]):
            if not node_queue:
                return
            res.append(node_queue[-1].val)
            size = len(node_queue)
            for _ in range(size):
                node = node_queue.popleft()
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            bfs(node_queue)

        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        bfs(queue)
        return res


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(1, left=TreeNode(2, right=TreeNode(5)), right=TreeNode(3, right=TreeNode(4)))
    result = solution.rightSideView(n)
    print(result)
    assert result == [1, 3, 4]

    n = TreeNode(1, right=TreeNode(3))
    result = solution.rightSideView(n)
    print(result)
    assert result == [1, 3]

    result = solution.rightSideView(None)
    print(result)
    assert result == []
