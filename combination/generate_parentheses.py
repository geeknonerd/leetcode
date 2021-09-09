"""
22. 括号生成
字符串 动态规划 回溯
中等


数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

有效括号组合需满足：左括号必须以正确的顺序闭合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 

提示：

1 <= n <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        s = []

        def backtrack(left, right):
            if len(s) == n * 2:
                ans.append(''.join(s))
                return
            if left < n:
                s.append('(')
                backtrack(left + 1, right)
                s.pop()
            if right < left:
                s.append(')')
                backtrack(left, right + 1)
                s.pop()
        backtrack(0, 0)
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.generateParenthesis(3)
    print(result)
    assert set(result) == set(["((()))", "(()())", "(())()", "()(())", "()()()"])

    result = solution.generateParenthesis(1)
    print(result)
    assert set(result) == set(["()"])
