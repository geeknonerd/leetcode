"""
28. 实现 strStr()
双指针 字符串 字符串匹配
简单


实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

 

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

 

示例 1：

输入：haystack = "hello", needle = "ll"
输出：2
示例 2：

输入：haystack = "aaaaa", needle = "bba"
输出：-1
示例 3：

输入：haystack = "", needle = ""
输出：0
 

提示：

1 <= haystack.length, needle.length <= 10^4
haystack 和 needle 仅由小写英文字符组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/implement-strstr
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left_size = len(haystack)
        right_size = len(needle)
        if left_size == 0 and right_size == 0:
            return 0
        if left_size < right_size:
            return -1
        for i in range(left_size):
            ori_index = i
            not_match = False
            for j in range(right_size):
                if ori_index >= left_size or needle[j] != haystack[ori_index]:
                    not_match = True
                    break
                ori_index += 1
            if not not_match:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()

    result = solution.strStr("hello", "ll")
    print(result)
    assert result == 2

    result = solution.strStr("aaaaa", "bba")
    print(result)
    assert result == -1

    result = solution.strStr("", "")
    print(result)
    assert result == 0
