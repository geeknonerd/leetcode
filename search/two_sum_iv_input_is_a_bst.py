"""
653. 两数之和 IV - 输入 BST
树 深度优先搜索 广度优先搜索 二叉搜索树 哈希表 双指针 二叉树
简单


给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

 

示例 1：


输入: root = [5,3,6,2,4,null,7], k = 9
输出: true
示例 2：


输入: root = [5,3,6,2,4,null,7], k = 28
输出: false
示例 3：

输入: root = [2,1,3], k = 4
输出: true
示例 4：

输入: root = [2,1,3], k = 1
输出: false
示例 5：

输入: root = [2,1,3], k = 3
输出: true
 

提示:

二叉树的节点个数的范围是  [1, 104].
-104 <= Node.val <= 104
root 为二叉搜索树
-105 <= k <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        num_set = set()

        def find(node: TreeNode, n_sum: int) -> bool:
            if not node:
                return False
            if (n_sum - node.val) in num_set:
                return True
            num_set.add(node.val)
            return find(node.left, n_sum) or find(node.right, n_sum)
        return find(root, k)


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(5,
                 left=TreeNode(3, left=TreeNode(2), right=TreeNode(4)),
                 right=TreeNode(6, right=TreeNode(7)))
    result = solution.findTarget(n, 9)
    print(result)
    assert result is True

    result = solution.findTarget(n, 28)
    print(result)
    assert result is False

    n = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    result = solution.findTarget(n, 4)
    print(result)
    assert result is True

    result = solution.findTarget(n, 1)
    print(result)
    assert result is False

    result = solution.findTarget(n, 3)
    print(result)
    assert result is True
