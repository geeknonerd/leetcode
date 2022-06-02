"""
258. 各位相加
数学 数论 模拟
简单


给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

 

示例 1:

输入: num = 38
输出: 2
解释: 各位相加的过程为：
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
由于 2 是一位数，所以返回 2。
示例 1:

输入: num = 0
输出: 0
 

提示：

0 <= num <= 2^31 - 1
 

进阶：你可以不使用循环或者递归，在 O(1) 时间复杂度内解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-digits
"""


class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num else 0


if __name__ == '__main__':
    solution = Solution()

    result = solution.addDigits(38)
    print(result)
    assert result == 2

    result = solution.addDigits(0)
    print(result)
    assert result == 0
