"""
516. 最长回文子序列
字符串 动态规划
中等


给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

 

示例 1：

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
示例 2：

输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。
 

提示：

1 <= s.length <= 1000
s 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        size = len(s)
        dp = [[0] * size for _ in range(size)]
        for i in range(size-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][size-1]


if __name__ == '__main__':
    solution = Solution()

    result = solution.longestPalindromeSubseq("bbbab")
    print(result)
    assert result == 4

    result = solution.longestPalindromeSubseq("cbbd")
    print(result)
    assert result == 2
