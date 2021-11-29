"""
451. 根据字符出现频率排序
哈希表 字符串 桶排序 计数 排序 堆（优先队列）
中等


给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:

输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
示例 2:

输入:
"cccaaa"

输出:
"cccaaa"

解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
示例 3:

输入:
"Aabb"

输出:
"bbAa"

解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-characters-by-frequency
"""
from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        s_dict = defaultdict(int)
        for c in s:
            s_dict[c] += 1
        s_list = sorted(s_dict.keys(), key=lambda x:s_dict[x], reverse=True)
        res = []
        for c in s_list:
            res.append(c*s_dict[c])
        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()

    result = solution.frequencySort("tree")
    print(result)
    assert result in ["eert", "eetr"]

    result = solution.frequencySort("cccaaa")
    print(result)
    assert result in ["cccaaa", "aaaccc"]

    result = solution.frequencySort("Aabb")
    print(result)
    assert result in ["bbAa", "bbaA"]
