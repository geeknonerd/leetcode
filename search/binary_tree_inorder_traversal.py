"""
94. 二叉树的中序遍历
栈 树 深度优先搜索 二叉树
简单


给定一个二叉树的根节点 root ，返回它的 中序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[2,1]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
 

进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(node: TreeNode):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        res = []
        inorder(root)
        return res


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    result = solution.inorderTraversal(n)
    print(result)
    assert result == [1, 3, 2]

    n = None
    result = solution.inorderTraversal(n)
    print(result)
    assert result == []

    n = TreeNode(1)
    result = solution.inorderTraversal(n)
    print(result)
    assert result == [1]

    n = TreeNode(1, left=TreeNode(2))
    result = solution.inorderTraversal(n)
    print(result)
    assert result == [2, 1]

    n = TreeNode(1, right=TreeNode(2))
    result = solution.inorderTraversal(n)
    print(result)
    assert result == [1, 2]
