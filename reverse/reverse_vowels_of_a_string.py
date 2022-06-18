"""
345. 反转字符串中的元音字母
双指针 字符串
简单


给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。

 

示例 1：

输入：s = "hello"
输出："holle"
示例 2：

输入：s = "leetcode"
输出："leotcede"
 

提示：

1 <= s.length <= 3 * 105
s 由 可打印的 ASCII 字符组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-vowels-of-a-string
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        r_indexs = []
        for i in range(len(s)):
            if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                r_indexs.append(i)
        r_len = len(r_indexs)
        for i in range(r_len):
            chars[r_indexs[i]] = s[r_indexs[r_len - i - 1]]
        return ''.join(chars)


if __name__ == '__main__':
    solution = Solution()

    result = solution.reverseVowels("hello")
    print(result)
    assert result == "holle"

    result = solution.reverseVowels("leetcode")
    print(result)
    assert result == "leotcede"

    result = solution.reverseVowels("aA")
    print(result)
    assert result == "Aa"

