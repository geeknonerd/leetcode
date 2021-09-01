"""
15. 三数之和
数组 双指针 排序
中等


给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]
 

提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for first in range(n):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            third = n - 1
            target = - nums[first]
            for second in range(first+1, n):
                if second > first + 1 and nums[second] == nums[second-1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.threeSum([-1, 0, 1, 2, -1, -4])
    print(result)
    assert {tuple(i) for i in result} == {tuple(i) for i in [[-1, -1, 2], [-1, 0, 1]]}

    result = solution.threeSum([])
    print(result)
    assert {tuple(i) for i in result} == {tuple(i) for i in []}

    result = solution.threeSum([0])
    print(result)
    assert {tuple(i) for i in result} == {tuple(i) for i in []}
