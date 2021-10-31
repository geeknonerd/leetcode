"""
108. 将有序数组转换为二叉搜索树
树 二叉搜索树 数组 分治 二叉树
简单


给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

 

示例 1：


输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

示例 2：


输入：nums = [1,3]
输出：[3,1]
解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。
 

提示：

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums 按 严格递增 顺序排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '{}({},{})'.format(self.val, self.left, self.right)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()

    result = solution.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(result)
    assert str(result) == '0(-10(None,-3(None,None)),5(None,9(None,None)))'

    result = solution.sortedArrayToBST([1, 3])
    print(result)
    assert str(result) == '1(None,3(None,None))'
