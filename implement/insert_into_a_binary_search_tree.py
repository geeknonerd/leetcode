"""
701. 二叉搜索树中的插入操作
树 二叉搜索树 二叉树
中等


给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。

注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。

 

示例 1：


输入：root = [4,2,7,1,3], val = 5
输出：[4,2,7,1,3,5]
解释：另一个满足题目要求可以通过的树是：

示例 2：

输入：root = [40,20,60,10,30,50,70], val = 25
输出：[40,20,60,10,30,50,70,null,null,25]
示例 3：

输入：root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
输出：[4,2,7,1,3,5]
 

 

提示：

给定的树上的节点数介于 0 和 10^4 之间
每个节点都有一个唯一整数值，取值范围从 0 到 10^8
-10^8 <= val <= 10^8
新值和原始二叉搜索树中的任意节点值都不同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-into-a-binary-search-tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '{},{},{}'.format(
            self.left if self.left else '-',
            self.val,
            self.right if self.right else '-')


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        cur = root
        while cur:
            if cur.val == val:
                break
            elif cur.val > val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    break
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = TreeNode(val)
                    break
                cur = cur.right
        return root


if __name__ == '__main__':
    solution = Solution()

    n = TreeNode(4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)), right=TreeNode(7))
    result = solution.insertIntoBST(n, 5)
    print(result)
    assert str(result) == '-,1,-,2,-,3,-,4,-,5,-,7,-'

    n = TreeNode(40,
                 left=TreeNode(20, left=TreeNode(10), right=TreeNode(30)),
                 right=TreeNode(60, left=TreeNode(50), right=TreeNode(70)))
    result = solution.insertIntoBST(n, 25)
    print(result)
    assert str(result) == '-,10,-,20,-,25,-,30,-,40,-,50,-,60,-,70,-'

    result = solution.insertIntoBST(None, 5)
    print(result)
    assert str(result) == '-,5,-'
