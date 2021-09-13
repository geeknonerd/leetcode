"""
139. 单词拆分
字典树 记忆化搜索 哈希表 字符串 动态规划
中等


给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        word_set = set(wordDict)
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and s[i:j] in word_set:
                    dp[j] = True
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()

    result = solution.wordBreak("leetcode", ["leet", "code"])
    print(result)
    assert result is True

    result = solution.wordBreak("applepenapple", ["apple", "pen"])
    print(result)
    assert result is True

    result = solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
    print(result)
    assert result is False
