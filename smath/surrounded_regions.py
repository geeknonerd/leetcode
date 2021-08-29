"""
130. 被围绕的区域
深度优先搜索 广度优先搜索 并查集 数组 矩阵
中等


给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
 

示例 1：


输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
示例 2：

输入：board = [["X"]]
输出：[["X"]]
 

提示：

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] 为 'X' 或 'O'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        n, m = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
                return
            board[x][y] = 'A'
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)

        for j in range(m):
            dfs(0, j)
            dfs(n-1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == '__main__':
    solution = Solution()

    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    solution.solve(board)
    print(board)
    assert board == [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]

    board = [["X"]]
    solution.solve(board)
    print(board)
    assert board == [["X"]]
