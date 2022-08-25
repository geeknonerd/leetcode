/*
349. 两个数组的交集
数组 哈希表 双指针 二分查找 排序
简单


给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。



示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的


提示：

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/intersection-of-two-arrays
*/
package main

import (
	"leetcode/go/utils"
	"sort"
)

func intersection(nums1 []int, nums2 []int) []int {
	sort.Ints(nums1)
	sort.Ints(nums2)
	var res []int
	n1Size := len(nums1)
	n2Size := len(nums2)
	i1 := 0
	i2 := 0
	for i1 < n1Size && i2 < n2Size {
		n1 := nums1[i1]
		n2 := nums2[i2]
		if n1 == n2 {
			resSize := len(res)
			if resSize == 0 || n1 != res[resSize-1] {
				res = append(res, n1)
			}
			i1 += 1
			i2 += 1
		} else if n1 > n2 {
			i2++
		} else {
			i1++
		}
	}
	return res
}

func main() {
	utils.Assert(intersection([]int{1, 2, 2, 1}, []int{2, 2}), []int{2})
	utils.Assert(intersection([]int{4, 9, 5}, []int{9, 4, 9, 8, 4}), []int{4, 9})
}
