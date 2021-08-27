"""
201. 数字范围按位与
位运算
中等


给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。

 

示例 1：

输入：left = 5, right = 7
输出：4
示例 2：

输入：left = 0, right = 0
输出：0
示例 3：

输入：left = 1, right = 2147483647
输出：0
 

提示：

0 <= left <= right <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range
"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift


if __name__ == '__main__':
    solution = Solution()

    result = solution.rangeBitwiseAnd(5, 7)
    print(result)
    assert result == 4

    result = solution.rangeBitwiseAnd(0, 0)
    print(result)
    assert result == 0

    result = solution.rangeBitwiseAnd(1, 2147483647)
    print(result)
    assert result == 0
