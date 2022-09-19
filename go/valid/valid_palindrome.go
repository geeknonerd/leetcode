/*
125. 验证回文串
双指针 字符串
简单


给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。



示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串
示例 2:

输入: "race a car"
输出: false
解释："raceacar" 不是回文串


提示：

1 <= s.length <= 2 * 10^5
字符串 s 由 ASCII 字符组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/valid-palindrome
*/
package main

import (
	"leetcode/go/utils"
)

func isAlphaOrNum(c uint8) bool {
	if (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9') {
		return true
	}
	return false
}

func toLower(c uint8) uint8 {
	if c >= 'A' && c <= 'Z' {
		return c + 32
	}
	return c
}

func isPalindrome(s string) bool {
	left := 0
	right := len(s) - 1
	for left < right {
		if !isAlphaOrNum(s[left]) {
			left++
			continue
		}
		if !isAlphaOrNum(s[right]) {
			right--
			continue
		}
		if toLower(s[left]) != toLower(s[right]) {
			return false
		}
		left++
		right--
	}
	return true
}

func main() {
	utils.Assert(isPalindrome("A man, a plan, a canal: Panama"), true)
	utils.Assert(isPalindrome("race a car"), false)
	utils.Assert(isPalindrome("0P"), false)
}
