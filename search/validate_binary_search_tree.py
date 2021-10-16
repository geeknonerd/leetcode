"""
98. 验证二叉搜索树
树 深度优先搜索 二叉搜索树 二叉树
中等


给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
 

示例 1：


输入：root = [2,1,3]
输出：true
示例 2：


输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
 

提示：

树中节点数目范围在[1, 104] 内
-2^31 <= Node.val <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node: TreeNode, min_val: int = -2 ** 32 - 1, max_val: int = 2 ** 32) -> bool:
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return valid(node.left, min_val=min_val, max_val=node.val) and \
                   valid(node.right, min_val=node.val, max_val=max_val)

        return valid(root)


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    result = solution.isValidBST(n)
    print(result)
    assert result is True

    n = TreeNode(5,
                 left=TreeNode(1),
                 right=TreeNode(4, left=TreeNode(3), right=TreeNode(6)))
    result = solution.isValidBST(n)
    print(result)
    assert result is False

    n = TreeNode(5,
                 left=TreeNode(4),
                 right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)))
    result = solution.isValidBST(n)
    print(result)
    assert result is False
