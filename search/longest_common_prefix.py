"""
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
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s_len = len(strs)
        if s_len == 0:
            return ''
        min_len = min([len(s) for s in strs])
        prefix_i = -1
        stop = False
        for i in range(min_len):
            for j in range(s_len-1):
                if strs[j][i] != strs[j+1][i]:
                    stop = True
                    break
            if stop:
                break
            prefix_i = i
        return strs[0][:prefix_i+1]


if __name__ == '__main__':
    solution = Solution()

    result = solution.longestCommonPrefix(["flower", "flow", "flight"])
    print(result)
    assert result == 'fl'

    result = solution.longestCommonPrefix(["dog", "racecar", "car"])
    print(result)
    assert result == ''
