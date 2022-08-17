/*
389. 找不同
位运算 哈希表 字符串 排序
简单


给定两个字符串 s 和 t ，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。



示例 1：

输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。
示例 2：

输入：s = "", t = "y"
输出："y"


提示：

0 <= s.length <= 1000
t.length == s.length + 1
s 和 t 只包含小写字母

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-the-difference
*/
package main

import (
	"leetcode/go/utils"
	"sort"
	"strings"
)

func sortString(s string) string {
	sArray := strings.Split(s, "")
	sort.Strings(sArray)
	return strings.Join(sArray, "")
}

func findTheDifference(s string, t string) byte {
	ss := sortString(s)
	st := sortString(t)
	stSize := len(st)
	for i := range st[:stSize-1] {
		if st[i] != ss[i] {
			return st[i]
		}
	}
	return st[stSize-1]
}

func main() {
	utils.Assert(findTheDifference("abcd", "abcde"), 'e')
	utils.Assert(findTheDifference("", "y"), 'y')
}
