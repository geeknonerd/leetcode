"""
784. 字母大小写全排列
位运算 字符串 回溯
中等


给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

 

示例：
输入：S = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

输入：S = "3z4"
输出：["3z4", "3Z4"]

输入：S = "12345"
输出：["12345"]
 

提示：

S 的长度不超过12。
S 仅由数字和字母组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-case-permutation
"""
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans: List[List[str]] = [[]]
        for c in s:
            n = len(ans)
            if c.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(c.upper())
                    ans[n+i].append(c.lower())
            else:
                for i in range(n):
                    ans[i].append(c)
        return list(map("".join, ans))


if __name__ == '__main__':
    solution = Solution()
    result = solution.letterCasePermutation("a1b2")
    print(result)
    assert set(result) == set(["a1b2", "a1B2", "A1b2", "A1B2"])

    result = solution.letterCasePermutation("3z4")
    print(result)
    assert set(result) == set(["3z4", "3Z4"])

    result = solution.letterCasePermutation("12345")
    print(result)
    assert set(result) == set(["12345"])
