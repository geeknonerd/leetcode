/*
342. 4的幂
位运算 递归 数学
简单


给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x



示例 1：

输入：n = 16
输出：true
示例 2：

输入：n = 5
输出：false
示例 3：

输入：n = 1
输出：true


提示：

-2^31 <= n <= 2^31 - 1


进阶：你能不使用循环或者递归来完成本题吗？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/power-of-four
*/
package main

import (
	"leetcode/go/utils"
)

func isPowerOfFour(n int) bool {
	if n == 1 {
		return true
	} else if n/4 <= 0 || n%4 != 0 {
		return false
	} else if n/4 == 1 && n%4 == 0 {
		return true
	}
	return isPowerOfFour(n / 4)
}

func main() {
	utils.Assert(isPowerOfFour(16), true)
	utils.Assert(isPowerOfFour(5), false)
	utils.Assert(isPowerOfFour(1), true)
}
