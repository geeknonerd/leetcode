"""
242. 有效的字母异位词
哈希表 字符串 排序
简单


给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

 

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
 

提示:

1 <= s.length, t.length <= 5 * 104
s 和 t 仅包含小写字母
 

进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-anagram
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [0] * 26
        t_list = [0] * 26
        start_i = ord('a')
        for c in s:
            s_list[ord(c)-start_i] += 1
        for c in t:
            t_list[ord(c)-start_i] += 1
        return s_list == t_list


if __name__ == '__main__':
    solution = Solution()

    result = solution.isAnagram("anagram", "nagaram")
    print(result)
    assert result is True

    result = solution.isAnagram("rat", "car")
    print(result)
    assert result is False
