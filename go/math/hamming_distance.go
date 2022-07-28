/*
461. 汉明距离
位运算
简单


两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 x 和 y，计算并返回它们之间的汉明距离。



示例 1：

输入：x = 1, y = 4
输出：2
解释：
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。
示例 2：

输入：x = 3, y = 1
输出：1


提示：

0 <= x, y <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/hamming-distance
*/
package main

import (
	"leetcode/go/utils"
	"strconv"
)

func hammingDistance(x int, y int) int {
	binStr := strconv.FormatInt(int64(x^y), 2)
	sum := 0
	for _, c := range binStr {
		if c == '1' {
			sum++
		}
	}
	return sum
}

func main() {
	utils.Assert(hammingDistance(1, 4), 2)
	utils.Assert(hammingDistance(3, 1), 1)
}
