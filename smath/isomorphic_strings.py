"""
205. 同构字符串
哈希表 字符串
简单


给定两个字符串 s 和 t ，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

 

示例 1:

输入：s = "egg", t = "add"
输出：true
示例 2：

输入：s = "foo", t = "bar"
输出：false
示例 3：

输入：s = "paper", t = "title"
输出：true
 

提示：

1 <= s.length <= 5 * 10^4
t.length == s.length
s 和 t 由任意有效的 ASCII 字符组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/isomorphic-strings
"""
from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def replace_str(ss):
            s_len = len(ss)
            s_dict = defaultdict(int)
            cur_i = 0
            s_list = [''] * s_len
            for i in range(s_len):
                si = ss[i]
                if si not in s_dict:
                    s_dict[si] = '[{}]'.format(cur_i)
                    cur_i += 1
                s_list[i] = s_dict[si]
            return ''.join(s_list)

        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        return replace_str(s) == replace_str(t)


if __name__ == '__main__':
    solution = Solution()

    result = solution.isIsomorphic("egg", "add")
    print(result)
    assert result is True

    result = solution.isIsomorphic("foo", "bar")
    print(result)
    assert result is False

    result = solution.isIsomorphic("paper", "title")
    print(result)
    assert result is True

    result = solution.isIsomorphic("bbbaaaba", "aaabbbba")
    print(result)
    assert result is False

    result = solution.isIsomorphic("badc", "baba")
    print(result)
    assert result is False

    result = solution.isIsomorphic("abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck")
    print(result)
    assert result is False
