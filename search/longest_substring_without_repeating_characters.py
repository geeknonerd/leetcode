"""
3. 无重复字符的最长子串
哈希表 字符串 滑动窗口
中等


给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        s_len = len(s)
        cur_len = 0
        max_len = 0
        lookup = set()
        left = 0
        for i in range(s_len):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len


if __name__ == '__main__':
    solution = Solution()

    result = solution.lengthOfLongestSubstring("abcabcbb")
    print(result)
    assert result == 3

    result = solution.lengthOfLongestSubstring("bbbbb")
    print(result)
    assert result == 1

    result = solution.lengthOfLongestSubstring("pwwkew")
    print(result)
    assert result == 3

    result = solution.lengthOfLongestSubstring("")
    print(result)
    assert result == 0

    result = solution.lengthOfLongestSubstring("lyudkewfsgzqfyvh")
    print(result)
    assert result == 12

    result = solution.lengthOfLongestSubstring("lyudkewfsgzqfyvhnsgfrridiklziern")
    print(result)
    assert result == 12
