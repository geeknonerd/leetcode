"""
459. 重复的子字符串
字符串 字符串匹配
简单


给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。

 

示例 1:

输入: s = "abab"
输出: true
解释: 可由子串 "ab" 重复两次构成。
示例 2:

输入: s = "aba"
输出: false
示例 3:

输入: s = "abcabcabcabc"
输出: true
解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
 

提示：

1 <= s.length <= 10^4
s 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/repeated-substring-pattern
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        if size < 2:
            return False
        for cur_size in range(1, size // 2 + 1):
            if s[cur_size] != s[0] or size % cur_size != 0:
                continue
            is_ok = True
            for i in range(cur_size, size):
                if s[i] != s[i % cur_size]:
                    is_ok = False
                    break
            if is_ok:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()

    result = solution.repeatedSubstringPattern("abab")
    print(result)
    assert result is True

    result = solution.repeatedSubstringPattern("aba")
    print(result)
    assert result is False

    result = solution.repeatedSubstringPattern("abcabcabcabc")
    print(result)
    assert result is True

    result = solution.repeatedSubstringPattern("aabaaba")
    print(result)
    assert result is False

