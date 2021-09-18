"""
149. 直线上最多的点数
几何 哈希表 数学
困难


给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。

 

示例 1：


输入：points = [[1,1],[2,2],[3,3]]
输出：3
示例 2：


输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4
 

提示：

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
points 中的所有点 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-points-on-a-line
"""
from typing import List
import math


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        if size <= 2:
            return size
        ret = 0
        for i in range(1, size):
            cnt_dict = {}
            for j in range(i):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                if dx == 0:
                    tmp = math.inf
                else:
                    if dy < 0:
                        dx = - dx
                        dy = - dy
                    tmp = dy / dx
                if tmp in cnt_dict:
                    cnt_dict[tmp] += 1
                else:
                    cnt_dict[tmp] = 1
            max_cnt = 0
            for v in cnt_dict.values():
                max_cnt = max(max_cnt, v + 1)
            ret = max(ret, max_cnt)
        return ret


if __name__ == '__main__':
    solution = Solution()

    result = solution.maxPoints([[1, 1], [2, 2], [3, 3]])
    print(result)
    assert result == 3

    result = solution.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]])
    print(result)
    assert result == 4

    result = solution.maxPoints([[0, 0], [1, -1], [1, 1]])
    print(result)
    assert result == 2
