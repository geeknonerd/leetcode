"""
79. 单词搜索
数组 回溯 矩阵
中等


给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例 1：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
示例 3：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
 

提示：

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board 和 word 仅由大小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i: int, j: int, k: int):
            if board[i][j] != word[k]:
                return False
            if k == size - 1:
                return True

            visited.add((i, j))
            res = False
            for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n:
                    if (ni, nj) not in visited:
                        if dfs(ni, nj, k+1):
                            res = True
                            break
            visited.remove((i, j))
            return res

        m, n = len(board), len(board[0])
        size = len(word)
        visited = set()
        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()

    result = solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
    print(result)
    assert result is True

    result = solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
    print(result)
    assert result is True

    result = solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")
    print(result)
    assert result is False
