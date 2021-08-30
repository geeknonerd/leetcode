"""
74. 搜索二维矩阵
数组 二分查找 矩阵
中等


编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
 

示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def matrix_value(index):
            i = index // n
            j = index % n
            return matrix[i][j]

        left = 0
        right = m * n - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = matrix_value(mid)
            if mid_val == target:
                return True
            elif mid_val > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    solution = Solution()

    result = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
    print(result)
    assert result is True

    result = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
    print(result)
    assert result is False
