"""
96. 不同的二叉搜索树
树 二叉搜索树 数学 动态规划 二叉树
中等


给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

 

示例 1：


输入：n = 3
输出：5
示例 2：

输入：n = 1
输出：1
 

提示：

1 <= n <= 19

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]


if __name__ == '__main__':
    solution = Solution()

    result = solution.numTrees(3)
    print(result)
    assert result == 5

    result = solution.numTrees(1)
    print(result)
    assert result == 1
