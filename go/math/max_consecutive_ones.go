/*
485. 最大连续 1 的个数
数组
简单


给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。



示例 1：

输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
示例 2:

输入：nums = [1,0,1,1,0,1]
输出：2


提示：

1 <= nums.length <= 10^5
nums[i] 不是 0 就是 1.

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/max-consecutive-ones
*/
package main

import (
	"leetcode/go/utils"
)

func maxVal(left int, right int) int {
	if left > right {
		return left
	}
	return right
}

func findMaxConsecutiveOnes(nums []int) int {
	curCnt := 0
	maxCnt := 0
	for _, v := range nums {
		if v == 1 {
			curCnt++
		} else {
			maxCnt = maxVal(maxCnt, curCnt)
			curCnt = 0
		}
	}
	maxCnt = maxVal(maxCnt, curCnt)
	return maxCnt
}

func main() {
	utils.Assert(findMaxConsecutiveOnes([]int{1, 1, 0, 1, 1, 1}), 3)
	utils.Assert(findMaxConsecutiveOnes([]int{1, 0, 1, 1, 0, 1}), 2)
}
