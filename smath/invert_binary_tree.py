"""
226. 翻转二叉树
树 深度优先搜索 广度优先搜索 二叉树
简单


翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '{}({},{})'.format(self.val, self.left if self.left else '', self.right if self.right else '')


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def switch(node: TreeNode):
            if not node:
                return node
            node.left, node.right = switch(node.right), switch(node.left)
            return node
        return switch(root)


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(4,
                 left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)),
                 right=TreeNode(7, left=TreeNode(6), right=TreeNode(9)))
    result = solution.invertTree(n)
    print(result)
    assert str(result) == '4(7(9(,),6(,)),2(3(,),1(,)))'
