/*
67. 二进制求和
位运算 数学 字符串 模拟
简单


给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。



示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"


提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-binary
*/
package main

import (
	"leetcode/go/utils"
	"strconv"
	"strings"
)

func getBinNum(s string, size int, i int) int {
	if i >= 0 && i < size && s[i] == '1' {
		return 1
	} else if i < 0 && i >= -size && s[size+i] == '1' {
		return 1
	}
	return 0
}

func addBinary(a string, b string) string {
	aSize := len(a)
	bSize := len(b)
	carryNum := 0
	var strArray []string
	for i := 1; i < aSize+1 || i < bSize+1; i++ {
		sum := getBinNum(a, aSize, -i) + getBinNum(b, bSize, -i) + carryNum
		strArray = append([]string{strconv.Itoa(sum % 2)}, strArray...)
		carryNum = sum / 2
	}
	if carryNum > 0 {
		strArray = append([]string{strconv.Itoa(carryNum)}, strArray...)
	}
	return strings.Join(strArray, "")
}

func main() {
	utils.Assert(addBinary("11", "1"), "100")
	utils.Assert(addBinary("1010", "1011"), "10101")
}
