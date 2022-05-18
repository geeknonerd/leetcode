"""
125. 验证回文串
双指针 字符串
简单


给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

 

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串
示例 2:

输入: "race a car"
输出: false
解释："raceacar" 不是回文串
 

提示：

1 <= s.length <= 2 * 10^5
字符串 s 由 ASCII 字符组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/valid-palindrome
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not ('A' <= s[left] <= 'Z' or 'a' <= s[left] <= 'z' or '0' <= s[left] <= '9'):
                left += 1
                continue
            if not ('A' <= s[right] <= 'Z' or 'a' <= s[right] <= 'z' or '0' <= s[right] <= '9'):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    solution = Solution()

    result = solution.isPalindrome("A man, a plan, a canal: Panama")
    print(result)
    assert result is True

    result = solution.isPalindrome("race a car")
    print(result)
    assert result is False

    result = solution.isPalindrome("0P")
    print(result)
    assert result is False
