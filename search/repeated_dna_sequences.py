"""
187. 重复的DNA序列
位运算 哈希表 字符串 滑动窗口 哈希函数 滚动哈希
中等


所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

 

示例 1：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC","CCCCCAAAAA"]
示例 2：

输入：s = "AAAAAAAAAAAAA"
输出：["AAAAAAAAAA"]
 

提示：

0 <= s.length <= 10^5
s[i] 为 'A'、'C'、'G' 或 'T'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-dna-sequences
"""
from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        size = 10
        ans = []
        cnt_dict = defaultdict(int)
        for i in range(len(s) - size + 1):
            sub = s[i: i + size]
            cnt_dict[sub] += 1
            if cnt_dict[sub] == 2:
                ans.append(sub)
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print(result)
    assert result == ["AAAAACCCCC", "CCCCCAAAAA"]

    result = solution.findRepeatedDnaSequences("AAAAAAAAAAAAA")
    print(result)
    assert result == ["AAAAAAAAAA"]
