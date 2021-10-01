"""
383. 赎金信
哈希表 字符串 计数
简单


给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)

 

示例 1：

输入：ransomNote = "a", magazine = "b"
输出：false
示例 2：

输入：ransomNote = "aa", magazine = "ab"
输出：false
示例 3：

输入：ransomNote = "aa", magazine = "aab"
输出：true
 

提示：

你可以假设两个字符串均只含有小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ransom-note
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        pd = [0] * 26
        s_s = ord('a')
        for s in magazine:
            pd[ord(s) - s_s] += 1
        for r in ransomNote:
            r_index = ord(r) - s_s
            if pd[r_index] < 1:
                return False
            else:
                pd[r_index] -= 1
        return True


if __name__ == '__main__':
    solution = Solution()

    result = solution.canConstruct('a', 'b')
    print(result)
    assert result is False

    result = solution.canConstruct('aa', 'ab')
    print(result)
    assert result is False

    result = solution.canConstruct('aa', 'aab')
    print(result)
    assert result is True
