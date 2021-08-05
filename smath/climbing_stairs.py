"""
70. 爬楼梯
记忆化搜索 数学 动态规划
简单


假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
"""


class Solution:
    memory_record = {}

    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        if n in self.memory_record:
            return self.memory_record.get(n)
        ans = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memory_record[n] = ans
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.climbStairs(2)
    print(result)
    assert result == 2

    result = solution.climbStairs(3)
    print(result)
    assert result == 3

    result = solution.climbStairs(6)
    print(result)
    assert result == 13
