"""
40. 组合总和 II
数组 回溯
中等


给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

注意：解集不能包含重复的组合。 

 

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
 

提示:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
"""
from typing import List, Set, Tuple


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, val):
            if val == 0:
                res.append(path[:])
                return
            for index in range(i, size):
                if candidates[index] > val:
                    break
                if index > i and candidates[index-1] == candidates[index]:
                    continue
                path.append(candidates[index])
                dfs(index + 1, val - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []
        path = []
        dfs(0, target)
        return res


def get_set(rl: List[List[int]]) -> Set[Tuple[int]]:
    ret = set()
    for i in rl:
        sorted(i)
        ret.add(tuple(i))
    return ret


if __name__ == '__main__':
    solution = Solution()

    result = solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print(result)
    assert get_set(result) == get_set([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])

    result = solution.combinationSum2([2, 5, 2, 1, 2], 5)
    print(result)
    assert get_set(result) == get_set([[1, 2, 2], [5]])
