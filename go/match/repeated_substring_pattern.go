/*
459. 重复的子字符串
字符串 字符串匹配
简单


给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。



示例 1:

输入: s = "abab"
输出: true
解释: 可由子串 "ab" 重复两次构成。
示例 2:

输入: s = "aba"
输出: false
示例 3:

输入: s = "abcabcabcabc"
输出: true
解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)


提示：

1 <= s.length <= 10^4
s 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/repeated-substring-pattern
*/
package main

import (
	"leetcode/go/utils"
)

func repeatedSubstringPattern(s string) bool {
	size := len(s)
	if size < 2 {
		return false
	}
	for subSize := 1; subSize < size/2+1; subSize++ {
		if s[subSize] != s[0] || size%subSize != 0 {
			continue
		}
		for i := subSize; i < size; i++ {
			if s[i] != s[i%subSize] {
				goto Next
			}
		}
		return true
	Next:
	}
	return false
}

func main() {
	utils.Assert(repeatedSubstringPattern("abab"), true)
	utils.Assert(repeatedSubstringPattern("aba"), false)
	utils.Assert(repeatedSubstringPattern("abcabcabcabc"), true)
	utils.Assert(repeatedSubstringPattern("aabaaba"), false)
}
