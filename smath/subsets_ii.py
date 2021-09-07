"""
90. 子集 II
位运算 数组 回溯
中等


给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

 

示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
 

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
"""
from typing import List, Set, Tuple


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        flags = set()
        for mask in range(1 << n):
            tmp = []
            for i in range(n):
                if mask & (1 << i):
                    tmp.append(nums[i])
            flag = ''.join((str(i) for i in tmp))
            if flag not in flags:
                ans.append(tmp)
                flags.add(flag)
        return ans


def get_set(rl: List[List[int]]) -> Set[Tuple[int]]:
    ret = set()
    for i in rl:
        sorted(i)
        ret.add(tuple(i))
    return ret


if __name__ == '__main__':
    solution = Solution()

    result = solution.subsetsWithDup([1, 2, 2])
    print(result)
    assert get_set(result) == get_set([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])

    result = solution.subsetsWithDup([0])
    print(result)
    assert get_set(result) == get_set([[], [0]])

    result = solution.subsetsWithDup([4, 4, 4, 1, 4])
    print(result)
    assert get_set(result) == get_set(
        [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]])
