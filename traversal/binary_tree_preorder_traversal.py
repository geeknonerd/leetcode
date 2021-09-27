"""
144. 二叉树的前序遍历
栈 树 深度优先搜索 二叉树
简单


给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,2,3]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[1,2]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
 

进阶：递归算法很简单，你可以通过迭代算法完成吗？



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '{}{}{}'.format(
            self.val,
            ',{}'.format(self.left) if self.left else '',
            ',{}'.format(self.right) if self.right else '')


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(node: TreeNode):
            if not node:
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        res = []
        preorder(root)
        return res


if __name__ == '__main__':
    solution = Solution()

    node = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    result = solution.preorderTraversal(node)
    print(result)
    assert ','.join([str(i) for i in result]) == '1,2,3'

    result = solution.preorderTraversal(None)
    print(result)
    assert ','.join([str(i) for i in result]) == ''

    node = TreeNode(1)
    result = solution.preorderTraversal(node)
    print(result)
    assert ','.join([str(i) for i in result]) == '1'

    node = TreeNode(1, left=TreeNode(2))
    result = solution.preorderTraversal(node)
    print(result)
    assert ','.join([str(i) for i in result]) == '1,2'

    node = TreeNode(1, right=TreeNode(2))
    result = solution.preorderTraversal(node)
    print(result)
    assert ','.join([str(i) for i in result]) == '1,2'
