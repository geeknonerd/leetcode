"""
105. 从前序与中序遍历序列构造二叉树
树 数组 哈希表 分治 二叉树
中等


给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。

 

示例 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
示例 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

提示:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder 和 inorder 均无重复元素
inorder 均出现在 preorder
preorder 保证为二叉树的前序遍历序列
inorder 保证为二叉树的中序遍历序列


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '{},{},{}'.format(self.val, self.left, self.right)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pre_left: int, pre_right: int, in_left: int, in_right: int):
            if pre_left > pre_right:
                return None
            pre_root = pre_left
            in_root = index[preorder[pre_root]]
            root = TreeNode(preorder[pre_root])
            size_left_sub = in_root - in_left
            root.left = build(pre_left + 1, pre_left + size_left_sub, in_left, in_root - 1)
            root.right = build(pre_left + size_left_sub + 1, pre_right, in_root + 1, in_right)
            return root

        n = len(preorder)
        index = {e: i for i, e in enumerate(inorder)}
        return build(0, n - 1, 0, n - 1)


if __name__ == '__main__':
    solution = Solution()

    result = solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(result)
    assert str(result) == '3,9,None,None,20,15,None,None,7,None,None'

    result = solution.buildTree([-1], [-1])
    print(result)
    assert str(result) == '-1,None,None'
