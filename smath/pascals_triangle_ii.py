"""
119. 杨辉三角 II
数组 动态规划
简单


给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。



 

示例 1:

输入: rowIndex = 3
输出: [1,3,3,1]
示例 2:

输入: rowIndex = 0
输出: [1]
示例 3:

输入: rowIndex = 1
输出: [1,1]
 

提示:

0 <= rowIndex <= 33
 

进阶：

你可以优化你的算法到 O(rowIndex) 空间复杂度吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [0] * (rowIndex + 1)
        row[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                row[j] += row[j-1]
        return row


if __name__ == '__main__':
    solution = Solution()

    result = solution.getRow(3)
    print(result)
    assert result == [1, 3, 3, 1]

    result = solution.getRow(0)
    print(result)
    assert result == [1]

    result = solution.getRow(1)
    print(result)
    assert result == [1, 1]
