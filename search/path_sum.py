"""
112. 路径总和
树 深度优先搜索 二叉树
简单


给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。

叶子节点 是指没有子节点的节点。

 

示例 1：


输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
示例 2：


输入：root = [1,2,3], targetSum = 5
输出：false
示例 3：

输入：root = [1,2], targetSum = 0
输出：false
 

提示：

树中节点的数目在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: TreeNode, val: int) -> bool:
            if not node:
                return False
            if node and not node.left and not node.right:
                if node.val == val:
                    return True
                else:
                    return False
            cur_val = val - node.val
            return dfs(node.left, cur_val) or dfs(node.right, cur_val)
        return dfs(root, targetSum)


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(5,
                 left=TreeNode(4,
                               left=TreeNode(11,
                                             left=TreeNode(7), right=TreeNode(2))),
                 right=TreeNode(8,
                                left=TreeNode(13),
                                right=TreeNode(4,
                                               right=TreeNode(1))))
    result = solution.hasPathSum(n, 22)
    print(result)
    assert result is True

    n = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    result = solution.hasPathSum(n, 5)
    print(result)
    assert result is False

    n = TreeNode(1, left=TreeNode(2))
    result = solution.hasPathSum(n, 0)
    print(result)
    assert result is False

    n = TreeNode(1, left=TreeNode(2))
    result = solution.hasPathSum(n, 1)
    print(result)
    assert result is False

