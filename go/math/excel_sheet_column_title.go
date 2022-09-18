/*
168. Excel表列名称
数学 字符串
简单


给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


示例 1：

输入：columnNumber = 1
输出："A"
示例 2：

输入：columnNumber = 28
输出："AB"
示例 3：

输入：columnNumber = 701
输出："ZY"
示例 4：

输入：columnNumber = 2147483647
输出："FXSHRXW"


提示：

1 <= columnNumber <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/excel-sheet-column-title
*/
package main

import (
	"leetcode/go/utils"
	"strings"
)

func convertToTitle(columnNumber int) string {
	var ts []string
	columnNumber--
	for columnNumber >= 26 {
		ts = append(ts, string(columnNumber%26+65))
		columnNumber = columnNumber/26 - 1
	}
	ts = append(ts, string(columnNumber+65))
	sb := strings.Builder{}
	for i := len(ts) - 1; i >= 0; i-- {
		sb.WriteString(ts[i])
	}
	return sb.String()
}

func main() {
	utils.Assert(convertToTitle(1), "A")
	utils.Assert(convertToTitle(28), "AB")
	utils.Assert(convertToTitle(701), "ZY")
	utils.Assert(convertToTitle(2147483647), "FXSHRXW")
	utils.Assert(convertToTitle(27), "AA")
}
