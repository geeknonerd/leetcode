"""
5. 最长回文子串
字符串 动态规划
中等


给你一个字符串 s，找到 s 中最长的回文子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        size = len(s)

        def expand(left, right):
            while left >= 0 and right < size and s[left] == s[right]:
                left -= 1
                right += 1
            return left+1, right-1

        for i in range(size):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i+1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start:end+1]


if __name__ == '__main__':
    solution = Solution()

    result = solution.longestPalindrome('babad')
    print(result)
    assert result == 'bab'

    result = solution.longestPalindrome('cbbd')
    print(result)
    assert result == 'bb'

    result = solution.longestPalindrome('a')
    print(result)
    assert result == 'a'

    result = solution.longestPalindrome('ac')
    print(result)
    assert result == 'a'
