"""
434. 字符串中的单词数
字符串
简单


统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:

输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/number-of-segments-in-a-string
"""


class Solution:
    def countSegments(self, s: str) -> int:
        scnt = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                scnt += 1
        return scnt


if __name__ == '__main__':
    solution = Solution()

    result = solution.countSegments("Hello, my name is John")
    print(result)
    assert result == 5
