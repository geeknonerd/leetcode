"""
450. 删除二叉搜索树中的节点
树 二叉搜索树 二叉树
中等


给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
 

示例 1:



输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
另一个正确答案是 [5,2,6,null,4,null,7]。


示例 2:

输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点
示例 3:

输入: root = [], key = 0
输出: []
 

提示:

节点数的范围 [0, 104].
-10^5 <= Node.val <= 10^5
节点值唯一
root 是合法的二叉搜索树
-10^5 <= key <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '{},{},{}'.format(self.val, self.left, self.right)


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def successor(r_node):
            r_node = r_node.right
            while r_node.left:
                r_node = r_node.left
            return r_node.val

        def predecessor(r_node):
            r_node = r_node.left
            while r_node.right:
                r_node = r_node.right
            return r_node.val

        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root


if __name__ == '__main__':
    solution = Solution()

    node = TreeNode(5, left=TreeNode(3, left=TreeNode(2), right=TreeNode(4)), right=TreeNode(6, right=TreeNode(7)))
    result = solution.deleteNode(node, 3)
    print(result)
    assert str(result) == '5,4,2,None,None,None,6,None,7,None,None'

    node = TreeNode(5, left=TreeNode(3, left=TreeNode(2), right=TreeNode(4)), right=TreeNode(6, right=TreeNode(7)))
    result = solution.deleteNode(node, 0)
    print(result)
    assert str(result) == '5,3,2,None,None,4,None,None,6,None,7,None,None'
