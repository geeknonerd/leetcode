"""
103. 二叉树的锯齿形层序遍历
树 广度优先搜索 二叉树
中等


给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
"""
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '{}({},{})'.format(self.val, self.left, self.right)


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def traversal(left_to_right):
            if not queue:
                return
            tmp = []
            for _ in range(len(queue)):
                if left_to_right:
                    tn = queue.popleft()
                else:
                    tn = queue.pop()
                tmp.append(tn.val)
                node_tuple = (tn.left, tn.right) if left_to_right else (tn.right, tn.left)
                for i in node_tuple:
                    if not i:
                        continue
                    if left_to_right:
                        queue.append(i)
                    else:
                        queue.appendleft(i)
            res.append(tmp)
            traversal(not left_to_right)

        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        traversal(True)
        return res


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    result = solution.zigzagLevelOrder(n)
    print(result)
    assert result == [
        [3],
        [20, 9],
        [15, 7]
    ]
