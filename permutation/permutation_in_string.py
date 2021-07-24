"""
567. 字符串的排列
哈希表 双指针 字符串
中等


给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的 子串 。

 

示例 1：

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
示例 2：

输入: s1= "ab" s2 = "eidboaoo"
输出: False
 

提示：

1 <= s1.length, s2.length <= 104
s1 和 s2 仅包含小写字母


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        a_ord = ord('a')
        for i in range(s1_len):
            cnt1[ord(s1[i])-a_ord] += 1
            cnt2[ord(s2[i])-a_ord] += 1
        if cnt1 == cnt2:
            return True
        i = s1_len
        while i < s2_len:
            cnt2[ord(s2[i])-a_ord] += 1
            cnt2[ord(s2[i-s1_len])-a_ord] -= 1
            if cnt1 == cnt2:
                return True
            i += 1
        return False


if __name__ == '__main__':
    solution = Solution()

    is_ok = solution.checkInclusion("ab", "eidbaooo")
    print(is_ok)
    assert is_ok is True

    is_ok = solution.checkInclusion("ab", "eidboaoo")
    print(is_ok)
    assert is_ok is False
