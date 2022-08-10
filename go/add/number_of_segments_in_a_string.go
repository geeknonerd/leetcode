/*
434. 字符串中的单词数
字符串
简单


统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:

输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/number-of-segments-in-a-string
*/
package main

import (
	"leetcode/go/utils"
)

func countSegments(s string) int {
	wordCnt := 0
	for i, v := range s {
		if (i == 0 || s[i-1] == ' ') && v != ' ' {
			wordCnt++
		}
	}
	return wordCnt
}

func main() {
	utils.Assert(countSegments("Hello, my name is John"), 5)
}
