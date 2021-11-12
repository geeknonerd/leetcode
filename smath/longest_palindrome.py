"""
409. 最长回文串
贪心 哈希表 字符串
简单


给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindrome
"""
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        cnt_dict = defaultdict(lambda: 0)
        for i in s:
            cnt_dict[i] += 1
        for v in cnt_dict.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.longestPalindrome("abccccdd")
    print(result)
    assert result == 7
