"""
231. 2 的幂
位运算 递归 数学
简单


给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

 

示例 1：

输入：n = 1
输出：true
解释：2^0 = 1
示例 2：

输入：n = 16
输出：true
解释：2^4 = 16
示例 3：

输入：n = 3
输出：false
示例 4：

输入：n = 4
输出：true
示例 5：

输入：n = 5
输出：false
 

提示：

-231 <= n <= 231 - 1
 

进阶：你能够不使用循环/递归解决此问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return self.recursion(n) if n > 0 else False

    def recursion(self, n) -> bool:
        if n == 1:
            return True
        elif n == 2:
            return True
        if n % 2 != 0:
            return False
        return self.recursion(n//2)


if __name__ == '__main__':
    solution = Solution()

    result = solution.isPowerOfTwo(1)
    print(result)
    assert result is True

    result = solution.isPowerOfTwo(16)
    print(result)
    assert result is True

    result = solution.isPowerOfTwo(3)
    print(result)
    assert result is False

    result = solution.isPowerOfTwo(4)
    print(result)
    assert result is True

    result = solution.isPowerOfTwo(5)
    print(result)
    assert result is False
