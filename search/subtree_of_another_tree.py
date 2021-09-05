"""
572. 另一棵树的子树
树 深度优先搜索 二叉树 字符串匹配 哈希函数
简单


给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。

二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。

 

示例 1：


输入：root = [3,4,5,1,2], subRoot = [4,1,2]
输出：true
示例 2：


输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
输出：false
 

提示：

root 树上的节点数量范围是 [1, 2000]
subRoot 树上的节点数量范围是 [1, 1000]
-10^4 <= root.val <= 10^4
-10^4 <= subRoot.val <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subtree-of-another-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def check(r, s):
            if not r and not s:
                return True
            if not r or not s or r.val != s.val:
                return False
            return check(r.left, s.left) and check(r.right, s.right)

        def dfs(r, s):
            if not r:
                return False
            return check(r, s) or dfs(r.left, s) or dfs(r.right, s)

        return dfs(root, subRoot)


if __name__ == '__main__':
    solution = Solution()

    r_node = TreeNode(3, left=TreeNode(4, left=TreeNode(1), right=TreeNode(2)), right=TreeNode(5))
    s_node = TreeNode(4, left=TreeNode(1), right=TreeNode(2))
    result = solution.isSubtree(r_node, s_node)
    print(result)
    assert result is True

    r_node = TreeNode(3, left=TreeNode(4, left=TreeNode(1), right=TreeNode(2, left=TreeNode(0))), right=TreeNode(5))
    s_node = TreeNode(4, left=TreeNode(1), right=TreeNode(2))
    result = solution.isSubtree(r_node, s_node)
    print(result)
    assert result is False



