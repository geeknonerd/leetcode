"""
290. 单词规律
哈希表 字符串
简单


给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。   

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        p_len = len(pattern)
        s_list_len = len(s_list)
        if p_len != s_list_len:
            return False
        exist_s = set()
        p_to_s_dict = {}
        for i in range(p_len):
            p = pattern[i]
            s = s_list[i]
            if p in p_to_s_dict:
                if p_to_s_dict[p] != s:
                    return False
            else:
                if s in exist_s:
                    return False
                else:
                    p_to_s_dict[p] = s
                    exist_s.add(s)
        return True


if __name__ == '__main__':
    solution = Solution()

    result = solution.wordPattern("abba", "dog cat cat dog")
    print(result)
    assert result is True

    result = solution.wordPattern("abba", "dog cat cat fish")
    print(result)
    assert result is False

    result = solution.wordPattern("aaaa", "dog cat cat dog")
    print(result)
    assert result is False

    result = solution.wordPattern("abba", "dog dog dog dog")
    print(result)
    assert result is False
