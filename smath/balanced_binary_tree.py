"""
110. 平衡二叉树
树 深度优先搜索 二叉树
简单


给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：true
示例 2：


输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
示例 3：

输入：root = []
输出：true
 

提示：

树中的节点数在范围 [0, 5000] 内
-10^4 <= Node.val <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/balanced-binary-tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def get_high(n: TreeNode) -> int:
            if not (n and n.val is not None):
                return 0
            return 1 + max(get_high(n.left), get_high(n.right))

        return -2 < get_high(root.left) - get_high(root.right) < 2 and self.isBalanced(root.left) \
               and self.isBalanced(root.right)


if __name__ == '__main__':
    solution = Solution()

    # [3, 9, 20, null, null, 15, 7]
    node = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    result = solution.isBalanced(node)
    print(result)
    assert result is True

    # [1,2,2,3,3,null,null,4,4]
    node = TreeNode(1, left=TreeNode(2, left=TreeNode(3, left=TreeNode(4), right=TreeNode(4)), right=TreeNode(3)),
                    right=TreeNode(2))
    result = solution.isBalanced(node)
    print(result)
    assert result is False

    # []
    node = None
    result = solution.isBalanced(node)
    print(result)
    assert result is True
