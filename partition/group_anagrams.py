"""
49. 字母异位词分组
哈希表 字符串 排序
中等


给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母都恰好只用一次。

 

示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:

输入: strs = [""]
输出: [[""]]
示例 3:

输入: strs = ["a"]
输出: [["a"]]
 

提示：

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
"""
from typing import List, Set, Tuple
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            mp[key].append(s)
        return list(mp.values())


def get_set(rl: List[List[int]]) -> Set[Tuple[int]]:
    ret = set()
    for i in rl:
        ret.add(tuple(sorted(i)))
    return ret


if __name__ == '__main__':
    solution = Solution()

    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)
    assert get_set(result) == get_set([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])

    result = solution.groupAnagrams([""])
    print(result)
    assert get_set(result) == get_set([[""]])

    result = solution.groupAnagrams(["a"])
    print(result)
    assert get_set(result) == get_set([["a"]])
