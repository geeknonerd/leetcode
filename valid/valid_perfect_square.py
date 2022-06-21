"""
367. 有效的完全平方数
数学 二分查找
简单


给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

进阶：不要 使用任何内置的库函数，如  sqrt 。

 

示例 1：

输入：num = 16
输出：true
示例 2：

输入：num = 14
输出：false
 

提示：

1 <= num <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/valid-perfect-square
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        i_sec = 1
        while i_sec <= num:

            if i_sec == num:
                return True
            elif i_sec < num:
                i += 1
            else:
                break
            i_sec = i * i
        return False


if __name__ == '__main__':
    solution = Solution()

    result = solution.isPerfectSquare(16)
    print(result)
    assert result is True

    result = solution.isPerfectSquare(14)
    print(result)
    assert result is False
