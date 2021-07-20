"""
557. 反转字符串中的单词 III
双指针 字符串
简单


给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

 

示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"
 

提示：

在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = [c for c in s]
        str_len = len(s)
        i = 0
        while i < str_len:
            start = i
            while i < str_len and str_list[i] != ' ':
                i += 1
            # reverse
            left = start
            right = i - 1
            # print(str_list[left: right+1])
            while left < right:
                str_list[left], str_list[right] = str_list[right], str_list[left]
                left += 1
                right -= 1
            while i < str_len and str_list[i] == ' ':
                i += 1
        return ''.join(str_list)


if __name__ == '__main__':
    solution = Solution()

    result = solution.reverseWords("Let's take LeetCode contest")
    print(result)
    assert result == "s'teL ekat edoCteeL tsetnoc"

    result = solution.reverseWords("God Ding")
    print(result)
    assert result == "doG gniD"
