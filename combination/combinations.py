"""
77. 组合
数组 回溯
中等


给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

 

示例 1：

输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
示例 2：

输入：n = 1, k = 1
输出：[[1]]
 

提示：

1 <= n <= 20
1 <= k <= n


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
"""
from typing import List


class Solution:

    def __init__(self):
        self.temp: List[int] = []
        self.ans: List[List[int]] = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.dfs(1, n, k)
        return self.ans

    def dfs(self, cur: int, n: int, k: int):
        if len(self.temp) + n - cur + 1 < k:
            return
        if len(self.temp) == k:
            self.ans.append(self.temp[:])
            return
        self.temp.append(cur)
        self.dfs(cur+1, n, k)
        self.temp.pop()
        self.dfs(cur+1, n, k)


if __name__ == '__main__':
    solution = Solution()

    result = solution.combine(4, 2)
    print(result)
    assert set((tuple(i) for i in result)) == set((tuple(i) for i in [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]))

    solution = Solution()
    result = solution.combine(1, 1)
    print(result)
    assert result == [[1]]
