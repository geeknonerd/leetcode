/*
171. Excel 表列序号
数学 字符串
简单


给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


示例 1:

输入: columnTitle = "A"
输出: 1
示例 2:

输入: columnTitle = "AB"
输出: 28
示例 3:

输入: columnTitle = "ZY"
输出: 701


提示：

1 <= columnTitle.length <= 7
columnTitle 仅由大写英文组成
columnTitle 在范围 ["A", "FXSHRXW"] 内

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/excel-sheet-column-number
*/
package main

import (
	"leetcode/go/utils"
	"math"
)

func titleToNumber(columnTitle string) int {
	var sum int
	size := len(columnTitle)
	for i := 0; i < size; i++ {
		sum += int(columnTitle[size-1-i]-64) * int(math.Pow(26, float64(i)))
	}
	return sum
}

func main() {
	utils.Assert(titleToNumber("A"), 1)
	utils.Assert(titleToNumber("AB"), 28)
	utils.Assert(titleToNumber("ZY"), 701)
}
