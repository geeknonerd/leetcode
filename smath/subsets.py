"""
78. 子集
位运算 数组 回溯
中等


给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
 

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for mask in range(1 << n):
            tmp = []
            for i in range(n):
                if mask & (1 << i):
                    tmp.append(nums[i])
            ans.append(tmp)
        return ans


def get_set_by_list(n_list):
    return {tuple for i in n_list}


if __name__ == '__main__':
    solution = Solution()

    result = solution.subsets([1, 2, 3])
    print(result)
    assert get_set_by_list(result) == get_set_by_list([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

    result = solution.subsets([0])
    print(result)
    assert get_set_by_list(result) == get_set_by_list([[], [0]])
