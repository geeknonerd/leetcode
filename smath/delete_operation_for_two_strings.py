"""
583. 两个字符串的删除操作
字符串 动态规划
中等


给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

 

示例：

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
 

提示：

给定单词的长度不超过500。
给定单词中的字符只含有小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        cached = {}

        def lcs(s1: str, s2: str, s1_len: int, s2_len: int) -> int:
            if not (s1_len and s2_len):
                return 0
            rc = cached.get((s1_len, s2_len))
            if rc is not None:
                return rc
            if s1[s1_len-1] == s2[s2_len-1]:
                res = 1 + lcs(s1, s2, s1_len-1, s2_len-1)
            else:
                res = max(lcs(s1, s2, s1_len-1, s2_len), lcs(s1, s2, s1_len, s2_len-1))
            cached[(s1_len, s2_len)] = res
            return res
        return len(word1) + len(word2) - 2*lcs(word1, word2, m, n)


if __name__ == '__main__':
    solution = Solution()

    result = solution.minDistance("sea", "eat")
    print(result)
    assert result == 2

    result = solution.minDistance("leetcode", "etco")
    print(result)
    assert result == 4

    result = solution.minDistance("park", "spake")
    print(result)
    assert result == 3
