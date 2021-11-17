"""
1249. 移除无效的括号
栈 字符串
中等


给你一个由 '('、')' 和小写字母组成的字符串 s。

你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。

请返回任意一个合法字符串。

有效「括号字符串」应当符合以下 任意一条 要求：

空字符串或只包含小写字母的字符串
可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」
可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」
 

示例 1：

输入：s = "lee(t(c)o)de)"
输出："lee(t(c)o)de"
解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。
示例 2：

输入：s = "a)b(c)d"
输出："ab(c)d"
示例 3：

输入：s = "))(("
输出：""
解释：空字符串也是有效的
示例 4：

输入：s = "(a(b(c)d)"
输出："a(b(c)d)"
 

提示：

1 <= s.length <= 10^5
s[i] 可能是 '('、')' 或英文小写字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-remove-to-make-valid-parentheses
"""
from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove_set = set()
        stack = deque()
        for i, c in enumerate(s):
            if c not in '()':
                continue
            if c == '(':
                stack.append(i)
            elif not stack:
                remove_set.add(i)
            else:
                stack.pop()
        remove_set = remove_set.union(set(stack))
        s_list = []
        for i, c in enumerate(s):
            if i not in remove_set:
                s_list.append(c)
        return ''.join(s_list)


if __name__ == '__main__':
    solution = Solution()

    result = solution.minRemoveToMakeValid("lee(t(c)o)de)")
    print(result)
    assert result in ("lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)")

    result = solution.minRemoveToMakeValid("a)b(c)d")
    print(result)
    assert result in ("ab(c)d",)

    result = solution.minRemoveToMakeValid("))((")
    print(result)
    assert result in ("",)

    result = solution.minRemoveToMakeValid("(a(b(c)d)")
    print(result)
    assert result in ("a(b(c)d)",)
