"""
387. 字符串中的第一个唯一字符
队列 哈希表 字符串 计数
简单


给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
 

提示：你可以假定该字符串只包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
"""
from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        size = len(s)
        frequency = OrderedDict()
        for i in range(size):
            if s[i] in frequency:
                frequency[s[i]] = -1
            else:
                frequency[s[i]] = i
        for i in frequency.values():
            if i != -1:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()

    result = solution.firstUniqChar("leetcode")
    print(result)
    assert result == 0

    result = solution.firstUniqChar("loveleetcode")
    print(result)
    assert result == 2

    result = solution.firstUniqChar("aadadaad")
    print(result)
    assert result == -1
