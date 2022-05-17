"""
111. 二叉树的最小深度
树 深度优先搜索 广度优先搜索 二叉树
简单


给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：2
示例 2：

输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
 

提示：

树中节点数的范围在 [0, 10^5] 内
-1000 <= Node.val <= 1000


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-depth-of-binary-tree
"""
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def is_leaf(n: TreeNode) -> bool:
            if n and not n.left and not n.right:
                return True
            return False

        def get_min_depth(n: TreeNode) -> int:
            if not n:
                return math.inf
            if is_leaf(n):
                return 1
            return 1 + min(get_min_depth(n.left), get_min_depth(n.right))

        ret = get_min_depth(root)
        return 0 if ret == math.inf else ret


if __name__ == '__main__':
    solution = Solution()

    # [3,9,20,null,null,15,7]
    node = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    result = solution.minDepth(node)
    print(result)
    assert result == 2

    # [2,null,3,null,4,null,5,null,6]
    node = TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5, right=TreeNode(6)))))
    result = solution.minDepth(node)
    print(result)
    assert result == 5
