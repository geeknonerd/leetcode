/*
219. 存在重复元素 II
数组 哈希表 滑动窗口
简单


给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。



示例 1：

输入：nums = [1,2,3,1], k = 3
输出：true
示例 2：

输入：nums = [1,0,1,1], k = 1
输出：true
示例 3：

输入：nums = [1,2,3,1,2,3], k = 2
输出：false




提示：

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/contains-duplicate-ii
*/
package main

import (
	"leetcode/go/utils"
)

func containsNearbyDuplicate(nums []int, k int) bool {
	pos := map[int]int{}
	for i, num := range nums {
		if p, ok := pos[num]; ok && i-p <= k {
			return true
		}
		pos[num] = i
	}
	return false
}

func main() {
	utils.Assert(containsNearbyDuplicate([]int{1, 2, 3, 1}, 3), true)
	utils.Assert(containsNearbyDuplicate([]int{1, 0, 1, 1}, 1), true)
	utils.Assert(containsNearbyDuplicate([]int{1, 2, 3, 1, 2, 3}, 2), false)
}
