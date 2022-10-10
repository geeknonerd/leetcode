/*
463. 岛屿的周长
深度优先搜索 广度优先搜索 数组 矩阵
简单


给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。

网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。



示例 1：



输入：grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
输出：16
解释：它的周长是上面图片中的 16 个黄色的边
示例 2：

输入：grid = [[1]]
输出：4
示例 3：

输入：grid = [[1,0]]
输出：4


提示：

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] 为 0 或 1


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/island-perimeter
*/
package main

import (
	"leetcode/go/utils"
)

func islandPerimeter(grid [][]int) int {
	dx := []int{0, 1, 0, -1}
	dy := []int{1, 0, -1, 0}
	n := len(grid)
	m := len(grid[0])
	ans := 0
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if grid[i][j] == 0 {
				continue
			}
			cnt := 0
			for d := 0; d < 4; d++ {
				tx := i + dx[d]
				ty := j + dy[d]
				if tx < 0 || tx >= n || ty < 0 || ty >= m || grid[tx][ty] == 0 {
					cnt++
				}
			}
			ans += cnt
		}
	}
	return ans
}

func main() {
	utils.Assert(islandPerimeter([][]int{{0, 1, 0, 0}, {1, 1, 1, 0}, {0, 1, 0, 0}, {1, 1, 0, 0}}), 16)
	utils.Assert(islandPerimeter([][]int{{1}}), 4)
	utils.Assert(islandPerimeter([][]int{{1, 0}}), 4)
	utils.Assert(islandPerimeter([][]int{{1, 1}}), 6)
}
