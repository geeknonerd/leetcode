/*
500. 键盘行
数组 哈希表 字符串


给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。




示例 1：

输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]
示例 2：

输入：words = ["omk"]
输出：[]
示例 3：

输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]


提示：

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] 由英文字母（小写和大写字母）组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/keyboard-row
*/
package main

import (
	"leetcode/go/utils"
	"unicode"
)

func findWords(words []string) (ans []string) {
	const rowIdx = "12210111011122000010020202"
next:
	for _, word := range words {
		idx := rowIdx[unicode.ToLower(rune(word[0]))-'a']
		for _, ch := range word[1:] {
			if rowIdx[unicode.ToLower(ch)-'a'] != idx {
				continue next
			}
		}
		ans = append(ans, word)
	}
	return ans
}

func main() {
	utils.Assert(findWords([]string{"Hello", "Alaska", "Dad", "Peace"}), []string{"Alaska", "Dad"})
	utils.Assert(findWords([]string{"omk"}), []string{})
	utils.Assert(findWords([]string{"adsdf", "sfd"}), []string{"adsdf", "sfd"})
}
