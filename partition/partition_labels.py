"""
763. 划分字母区间
贪心 哈希表 双指针 字符串
中等


字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

 

示例：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
 

提示：

S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-labels
"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pass


if __name__ == '__main__':
    solution = Solution()

    result = solution.partitionLabels("ababcbacadefegdehijhklij")
    print(result)
    assert result == [9, 7, 8]
