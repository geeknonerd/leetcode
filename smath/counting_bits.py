"""
338. 比特位计数
位运算 动态规划
简单


给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

 

示例 1：

输入：n = 2
输出：[0,1,1]
解释：
0 --> 0
1 --> 1
2 --> 10
示例 2：

输入：n = 5
输出：[0,1,1,2,1,2]
解释：
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

提示：

0 <= n <= 10^5
 

进阶：

很容易就能实现时间复杂度为 O(n log n) 的解决方案，你可以在线性时间复杂度 O(n) 内用一趟扫描解决此问题吗？
你能不使用任何内置函数解决此问题吗？（如，C++ 中的 __builtin_popcount ）

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/counting-bits
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0]
        for i in range(1, n+1):
            bits.append(bits[i >> 1] + (i & 1))
        return bits


if __name__ == '__main__':
    solution = Solution()

    result = solution.countBits(2)
    print(result)
    assert result == [0, 1, 1]

    result = solution.countBits(5)
    print(result)
    assert result == [0, 1, 1, 2, 1, 2]
