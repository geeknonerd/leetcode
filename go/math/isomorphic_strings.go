/*
205. 同构字符串
哈希表 字符串
简单


给定两个字符串 s 和 t ，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。



示例 1:

输入：s = "egg", t = "add"
输出：true
示例 2：

输入：s = "foo", t = "bar"
输出：false
示例 3：

输入：s = "paper", t = "title"
输出：true


提示：

1 <= s.length <= 5 * 10^4
t.length == s.length
s 和 t 由任意有效的 ASCII 字符组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/isomorphic-strings
*/
package main

import (
	"fmt"
	"leetcode/go/utils"
	"strings"
)

func replaceFmtStr(s string) string {
	sb := strings.Builder{}
	sMap := make(map[uint8]string)
	cur := 0
	for i := 0; i < len(s); i++ {
		v, ok := sMap[s[i]]
		if !ok {
			v = fmt.Sprintf("|%d", cur)
			sMap[s[i]] = v
			cur++
		}
		sb.WriteString(v)
	}
	return sb.String()
}

func isIsomorphic(s string, t string) bool {
	return replaceFmtStr(s) == replaceFmtStr(t)
}

func main() {
	utils.Assert(isIsomorphic("egg", "add"), true)
	utils.Assert(isIsomorphic("foo", "bar"), false)
	utils.Assert(isIsomorphic("paper", "title"), true)
	utils.Assert(isIsomorphic("bbbaaaba", "aaabbbba"), false)
	utils.Assert(isIsomorphic("badc", "baba"), false)
	utils.Assert(isIsomorphic("abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck"), false)
}
