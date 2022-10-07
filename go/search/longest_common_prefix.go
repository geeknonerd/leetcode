/*
14. 最长公共前缀
字符串
简单


编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


提示：

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
*/
package main

import (
	"leetcode/go/utils"
)

func longestCommonPrefix(strs []string) string {
	sSize := len(strs)
	minSize := 200
	for _, s := range strs {
		size := len(s)
		if size < minSize {
			minSize = size
		}
	}
	stop := false
	index := -1
	for i := 0; i < minSize; i++ {
		for j := 0; j < sSize-1; j++ {
			if strs[j][i] != strs[j+1][i] {
				stop = true
			}
		}
		if stop {
			break
		}
		index = i
	}
	return strs[0][:index+1]
}

func main() {
	utils.Assert(longestCommonPrefix([]string{"flower", "flow", "flight"}), "fl")
	utils.Assert(longestCommonPrefix([]string{"dog", "racecar", "car"}), "")
}
