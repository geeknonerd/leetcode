"""
303. 区域和检索 - 数组不可变
设计 数组 前缀和
简单


给定一个整数数组  nums，处理以下类型的多个查询:

计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right
实现 NumArray 类：

NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )
 

示例 1：

输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]

解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
 

提示：

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= i <= j < nums.length
最多调用 104 次 sumRange 方法

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/range-sum-query-immutable
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        sum_list = [nums[0]]
        for i in range(1, len(nums)):
            sum_list.append(sum_list[i-1] + nums[i])
        self.sum_list = sum_list

    def sumRange(self, left: int, right: int) -> int:
        diff = 0
        if left > 0:
            diff = self.sum_list[left-1]
        return self.sum_list[right] - diff


if __name__ == '__main__':
    solution = NumArray([-2, 0, 3, -5, 2, -1])
    assert solution.sumRange(0, 2) == 1
    assert solution.sumRange(2, 5) == -1
    assert solution.sumRange(0, 5) == -3
