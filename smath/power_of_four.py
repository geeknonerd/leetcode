"""
342. 4的幂
位运算 递归 数学
简单


给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x

 

示例 1：

输入：n = 16
输出：true
示例 2：

输入：n = 5
输出：false
示例 3：

输入：n = 1
输出：true
 

提示：

-2^31 <= n <= 2^31 - 1
 

进阶：你能不使用循环或者递归来完成本题吗？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/power-of-four
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and (n & (n-1) == 0) and n % 3 == 1
        if n == 1:
            return True
        if n // 4 <= 0 or n % 4 != 0:
            return False
        if n // 4 == 1:
            return True
        return self.isPowerOfFour(n // 4)


if __name__ == '__main__':
    solution = Solution()

    result = solution.isPowerOfFour(16)
    print(result)
    assert result is True

    result = solution.isPowerOfFour(5)
    print(result)
    assert result is False

    result = solution.isPowerOfFour(1)
    print(result)
    assert result is True

