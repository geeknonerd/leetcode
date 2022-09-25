/*
66. 加一
数组 数学
简单


给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。



示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：

输入：digits = [0]
输出：[1]


提示：

1 <= digits.length <= 100
0 <= digits[i] <= 9

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/plus-one
*/
package main

import (
	"leetcode/go/utils"
)

func plusOne(digits []int) []int {
	newDigits := digits[:]
	addVal := 1
	for i := len(newDigits) - 1; i >= 0; i-- {
		newVal := newDigits[i] + addVal
		if newVal > 9 {
			addVal = 1
			newVal = newVal % 10
		} else {
			addVal = 0
		}
		newDigits[i] = newVal
	}
	if addVal > 0 {
		newDigits = append([]int{addVal}, newDigits...)
	}
	return newDigits
}

func main() {
	utils.Assert(plusOne([]int{1, 2, 3}), []int{1, 2, 4})
	utils.Assert(plusOne([]int{4, 3, 2, 1}), []int{4, 3, 2, 2})
	utils.Assert(plusOne([]int{0}), []int{1})
	utils.Assert(plusOne([]int{1, 9, 9}), []int{2, 0, 0})
	utils.Assert(plusOne([]int{9, 9}), []int{1, 0, 0})
}
