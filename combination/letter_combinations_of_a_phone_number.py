"""
17. 电话号码的字母组合
哈希表 字符串 回溯
中等


给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



 

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]
 

提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
"""
from typing import List


class Solution:
    num_letter_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits: str) -> List[str]:
        size = len(digits)
        ans = []
        ltr_list = []

        def dfs(cur: int):
            if cur == size:
                if ltr_list:
                    ans.append(''.join(ltr_list))
                return
            letters = self.num_letter_dict[digits[cur]]
            for ltr in letters:
                ltr_list.append(ltr)
                dfs(cur + 1)
                ltr_list.pop()

        dfs(0)
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.letterCombinations("23")
    print(result)
    assert set(result) == set(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

    result = solution.letterCombinations("")
    print(result)
    assert set(result) == set([])

    result = solution.letterCombinations("2")
    print(result)
    assert set(result) == set(["a", "b", "c"])
