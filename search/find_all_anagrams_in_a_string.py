"""
438. 找到字符串中所有字母异位词
哈希表 字符串 滑动窗口
中等


给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指字母相同，但排列不同的字符串。

 

示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
 

提示:

1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
"""
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)
        ans = []
        if not (s and p and p_len <= s_len):
            return ans
        s_char_cnt = [0] * 26
        p_char_cnt = [0] * 26
        a_ord = ord('a')
        for i in range(p_len):
            p_char_cnt[ord(p[i]) - a_ord] += 1
            s_char_cnt[ord(s[i]) - a_ord] += 1
        if s_char_cnt == p_char_cnt:
            ans.append(0)
        for j in range(p_len, s_len):
            s_char_cnt[ord(s[j - p_len]) - a_ord] -= 1
            s_char_cnt[ord(s[j]) - a_ord] += 1
            if s_char_cnt == p_char_cnt:
                ans.append(j - p_len + 1)
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.findAnagrams("cbaebabacd", "abc")
    print(result)
    assert result == [0, 6]

    result = solution.findAnagrams("abab", "ab")
    print(result)
    assert result == [0, 1, 2]
