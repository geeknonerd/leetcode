/*
345. 反转字符串中的元音字母
双指针 字符串
简单


给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。



示例 1：

输入：s = "hello"
输出："holle"
示例 2：

输入：s = "leetcode"
输出："leotcede"


提示：

1 <= s.length <= 3 * 105
s 由 可打印的 ASCII 字符组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-vowels-of-a-string
*/
package main

import (
	"leetcode/go/utils"
	"unicode"
)

func reverseVowels(s string) string {
	var chars []rune
	var cis []int
	for i, c := range s {
		cl := unicode.ToLower(c)
		if cl == 'a' || cl == 'e' || cl == 'i' || cl == 'o' || cl == 'u' {
			cis = append(cis, i)
		}
		chars = append(chars, c)
	}
	ciSize := len(cis)
	for i := 0; i < ciSize; i++ {
		chars[cis[i]] = rune(s[cis[ciSize-1-i]])
	}
	return string(chars)
}

func main() {
	utils.Assert(reverseVowels("hello"), "holle")
	utils.Assert(reverseVowels("leetcode"), "leotcede")
	utils.Assert(reverseVowels("aA"), "Aa")
}
