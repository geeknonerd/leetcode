"""
47. 全排列 II
数组 回溯
中等


给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

 

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return []
        path = []
        res = []
        used = [False] * size
        nums.sort()

        def dfs(cur: int):
            if cur == size:
                res.append(path[:])
                return
            for i in range(size):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs(cur + 1)
                used[i] = False
                path.pop()

        dfs(0)
        return res


def get_set_by_list(n_list):
    return {tuple for i in n_list}


if __name__ == '__main__':
    solution = Solution()

    result = solution.permuteUnique([1, 1, 2])
    print(result)
    assert get_set_by_list(result) == get_set_by_list([[1, 1, 2], [1, 2, 1], [2, 1, 1]])

    result = solution.permuteUnique([1, 2, 3])
    print(result)
    assert get_set_by_list(result) == get_set_by_list(
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
