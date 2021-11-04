"""
997. 找到小镇的法官
图 数组 哈希表
简单


在一个小镇里，按从 1 到 n 为 n 个人进行编号。传言称，这些人中有一个是小镇上的秘密法官。

如果小镇的法官真的存在，那么：

小镇的法官不相信任何人。
每个人（除了小镇法官外）都信任小镇的法官。
只有一个人同时满足条件 1 和条件 2 。
给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示编号为 a 的人信任编号为 b 的人。

如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的编号。否则，返回 -1。

 

示例 1：

输入：n = 2, trust = [[1,2]]
输出：2
示例 2：

输入：n = 3, trust = [[1,3],[2,3]]
输出：3
示例 3：

输入：n = 3, trust = [[1,3],[2,3],[3,1]]
输出：-1
示例 4：

输入：n = 3, trust = [[1,2],[2,3]]
输出：-1
示例 5：

输入：n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
输出：3
 

提示：

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
trust[i] 互不相同
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-town-judge
"""
from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1
        trust_cnt_dict = defaultdict(lambda: [0, 0])
        for s, t in trust:
            trust_cnt_dict[t][0] += 1
            trust_cnt_dict[s][1] += 1
        for k, v in trust_cnt_dict.items():
            if v[0] == n - 1 and v[1] == 0:
                return k
        return -1


if __name__ == '__main__':
    solution = Solution()

    result = solution.findJudge(2, [[1, 2]])
    print(result)
    assert result == 2

    result = solution.findJudge(3, [[1, 3], [2, 3]])
    print(result)
    assert result == 3

    result = solution.findJudge(3, [[1, 3], [2, 3], [3, 1]])
    print(result)
    assert result == -1

    result = solution.findJudge(3, [[1, 2], [2, 3]])
    print(result)
    assert result == -1

    result = solution.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])
    print(result)
    assert result == 3

    result = solution.findJudge(1, [])
    print(result)
    assert result == 1
