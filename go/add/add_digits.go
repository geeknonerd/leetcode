/*
258. 各位相加
数学 数论 模拟
简单


给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。



示例 1:

输入: num = 38
输出: 2
解释: 各位相加的过程为：
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
由于 2 是一位数，所以返回 2。
示例 1:

输入: num = 0
输出: 0


提示：

0 <= num <= 2^31 - 1


进阶：你可以不使用循环或者递归，在 O(1) 时间复杂度内解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-digits
*/
package main

import (
	"leetcode/go/utils"
)

func addDigits(num int) int {
	if num == 0 {
		return 0
	}
	return (num-1)%9 + 1
}

func main() {
	utils.Assert(addDigits(38), 2)
	utils.Assert(addDigits(0), 0)
}
