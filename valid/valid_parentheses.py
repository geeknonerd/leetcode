"""
20. 有效的括号
栈 字符串
简单


给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 

示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true
 

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
"""
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        match_dict = {
            ')': '(', ']': '[', '}': '{'
        }
        left_list = match_dict.values()
        stack = deque()
        for c in s:
            if c in left_list:
                stack.append(c)
            elif c in match_dict:
                if not stack:
                    return False
                pop_c = stack.pop()
                if pop_c != match_dict[c]:
                    return False
        if stack:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()

    result = solution.isValid("()")
    print(result)
    assert result is True

    result = solution.isValid("()[]{}")
    print(result)
    assert result is True

    result = solution.isValid("(]")
    print(result)
    assert result is False

    result = solution.isValid("([)]")
    print(result)
    assert result is False

    result = solution.isValid("{[]}")
    print(result)
    assert result is True

    result = solution.isValid("]")
    print(result)
    assert result is False
