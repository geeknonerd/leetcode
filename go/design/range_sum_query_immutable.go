/*
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

1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
0 <= i <= j < nums.length
最多调用 10^4 次 sumRange 方法

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/range-sum-query-immutable
*/
package main

import "leetcode/go/utils"

type NumArray struct {
	sums []int
}

func Constructor(nums []int) NumArray {
	sums := nums[:1]
	size := len(nums)
	for i := 1; i < size; i++ {
		sums = append(sums, sums[i-1]+nums[i])
	}
	return NumArray{sums: sums}
}

func (this *NumArray) SumRange(left int, right int) int {
	diff := 0
	if left > 0 {
		diff = this.sums[left-1]
	}
	return this.sums[right] - diff
}

func main() {
	obj := Constructor([]int{-2, 0, 3, -5, 2, -1})
	utils.Assert(obj.SumRange(0, 2), 1)
	utils.Assert(obj.SumRange(2, 5), -1)
	utils.Assert(obj.SumRange(0, 5), -3)
}
