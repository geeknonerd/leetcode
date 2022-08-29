/*
326. 3 的幂
递归 数学
简单


给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x



示例 1：

输入：n = 27
输出：true
示例 2：

输入：n = 0
输出：false
示例 3：

输入：n = 9
输出：true
示例 4：

输入：n = 45
输出：false


提示：

-2^31 <= n <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/power-of-three
*/
package main

import (
	"leetcode/go/utils"
)

func isPowerOfThree(n int) bool {
	if n == 1 {
		return true
	} else if n/3 == 1 && n%3 == 0 {
		return true
	} else if n/3 < 1 || n%3 != 0 {
		return false
	}
	return isPowerOfThree(n / 3)
}

func main() {
	utils.Assert(isPowerOfThree(27), true)
	utils.Assert(isPowerOfThree(0), false)
	utils.Assert(isPowerOfThree(9), true)
	utils.Assert(isPowerOfThree(45), false)
	utils.Assert(isPowerOfThree(1), true)
}
