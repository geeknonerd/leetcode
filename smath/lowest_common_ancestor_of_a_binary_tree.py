"""
236. 二叉树的最近公共祖先
树 深度优先搜索 二叉树
中等


给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

 

示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例 2：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
示例 3：

输入：root = [1,2], p = 1, q = 2
输出：1
 

提示：

树中节点数目在范围 [2, 105] 内。
-10^9 <= Node.val <= 10^9
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
"""


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans: TreeNode = None

        def dfs(node: 'TreeNode', np: 'TreeNode', nq: 'TreeNode') -> bool:
            nonlocal ans
            if not node:
                return False
            lson = dfs(node.left, np, nq)
            rson = dfs(node.right, np, nq)
            if (lson and rson) or ((node.val == np.val or node.val == nq.val) and (lson or rson)):
                ans = node
            return lson or rson or (node.val == np.val or node.val == nq.val)

        dfs(root, p, q)
        return ans


if __name__ == '__main__':
    solution = Solution()

    tree = TreeNode(3, left=TreeNode(5, left=TreeNode(6), right=TreeNode(2, left=TreeNode(7), right=TreeNode(4))),
                    right=TreeNode(1, left=TreeNode(0), right=TreeNode(8)))
    result = solution.lowestCommonAncestor(tree, TreeNode(5), TreeNode(1))
    print(result.val if result else None)
    assert result and result.val == 3

    result = solution.lowestCommonAncestor(tree, TreeNode(5), TreeNode(4))
    print(result.val if result else None)
    assert result and result.val == 5

    tree = TreeNode(1, left=TreeNode(2))
    result = solution.lowestCommonAncestor(tree, TreeNode(1), TreeNode(2))
    print(result.val if result else None)
    assert result and result.val == 1
