/*
28. 实现 strStr()
双指针 字符串 字符串匹配
简单


实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。



说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。



示例 1：

输入：haystack = "hello", needle = "ll"
输出：2
示例 2：

输入：haystack = "aaaaa", needle = "bba"
输出：-1
示例 3：

输入：haystack = "", needle = ""
输出：0


提示：

1 <= haystack.length, needle.length <= 10^4
haystack 和 needle 仅由小写英文字符组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/implement-strstr
*/
package main

import (
	"leetcode/go/utils"
)

func strStr(haystack string, needle string) int {
	hSize := len(haystack)
	nSize := len(needle)
	if nSize == 0 {
		return 0
	}
	if hSize < nSize {
		return -1
	}
	for i := 0; i < hSize; i++ {
		si := i
		match := true
		for j := 0; j < nSize; j++ {
			if si >= hSize || needle[j] != haystack[si] {
				match = false
				break
			}
			si++
		}
		if match {
			return i
		}
	}
	return -1
}

func main() {
	utils.Assert(strStr("hello", "ll"), 2)
	utils.Assert(strStr("aaaaa", "bba"), -1)
	utils.Assert(strStr("", ""), 0)
}
