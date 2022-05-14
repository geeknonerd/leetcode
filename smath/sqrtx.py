"""
69. x 的平方根
数学 二分查找
容易


给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

 

示例 1：

输入：x = 4
输出：2
示例 2：

输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
 

提示：

0 <= x <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sqrtx
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        c, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + c/x0)
            if abs(x0 - xi) < 1e-6:
                break
            x0 = xi
        return int(x0)


if __name__ == '__main__':
    solution = Solution()

    result = solution.mySqrt(4)
    print(result)
    assert result == 2

    result = solution.mySqrt(8)
    print(result)
    assert result == 2
