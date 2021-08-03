"""
46. 全排列
数组 回溯
中等


给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

 

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
 

提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first: int = 0):
            if first >= n - 1:
                res.append(nums[:])
                return
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


if __name__ == '__main__':
    solution = Solution()

    result = solution.permute([1, 2, 3])
    print(result)
    assert set((tuple(i) for i in result)) == set(
        (tuple(i) for i in [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]))

    result = solution.permute([0, 1])
    print(result)
    assert set((tuple(i) for i in result)) == set(
        (tuple(i) for i in [[0, 1], [1, 0]]))

    result = solution.permute([1])
    print(result)
    assert set((tuple(i) for i in result)) == set(
        (tuple(i) for i in [[1]]))
