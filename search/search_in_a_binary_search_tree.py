"""
700. 二叉搜索树中的搜索
树 二叉搜索树 二叉树
简单


给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

例如，

给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和值: 2
你应该返回如下子树:

      2
     / \
    1   3
在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-a-binary-search-tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '{}({},{})'.format(self.val, self.left if self.left else '', self.right if self.right else '')


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return root
        if root.val == val:
            return root
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(4,
                 left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)),
                 right=TreeNode(7))
    result = solution.searchBST(n, 2)
    print(result)
    assert str(result) == '2(1(,),3(,))'

    result = solution.searchBST(n, 5)
    print(result)
    assert str(result) == 'None'
