"""
100. 相同的树
树 深度优先搜索 广度优先搜索 二叉树
简单


给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

 

示例 1：


输入：p = [1,2,3], q = [1,2,3]
输出：true
示例 2：


输入：p = [1,2], q = [1,null,2]
输出：false
示例 3：


输入：p = [1,2,1], q = [1,1,2]
输出：false
 

提示：

两棵树上的节点数目都在范围 [0, 100] 内
-10^4 <= Node.val <= 10^4


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/same-tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def is_same_node(l: TreeNode, r: TreeNode) -> bool:
            if l is None or r is None:
                return l == r
            if l.val != r.val:
                return False
            return is_same_node(l.left, r.left) and is_same_node(l.right, r.right)
        return is_same_node(p, q)


if __name__ == '__main__':
    solution = Solution()

    left = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    right = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    result = solution.isSameTree(left, right)
    print(result)
    assert result is True

    left = TreeNode(1, left=TreeNode(2))
    right = TreeNode(1, right=TreeNode(2))
    result = solution.isSameTree(left, right)
    print(result)
    assert result is False

    left = TreeNode(1, left=TreeNode(2), right=TreeNode(1))
    right = TreeNode(1, left=TreeNode(1), right=TreeNode(2))
    result = solution.isSameTree(left, right)
    print(result)
    assert result is False
