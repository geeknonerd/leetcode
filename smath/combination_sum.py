"""
39. 组合总和
数组 回溯
中等


给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。

candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 

对于给定的输入，保证和为 target 的唯一组合数少于 150 个。

 

示例 1：

输入: candidates = [2,3,6,7], target = 7
输出: [[7],[2,2,3]]
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []
示例 4：

输入: candidates = [1], target = 1
输出: [[1]]
示例 5：

输入: candidates = [1], target = 2
输出: [[1,1]]
 

提示：

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
"""
from typing import List, Set, Tuple


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        cur_list = []
        ans = []

        def dfs(t, i):
            if i == size:
                return
            if t == 0:
                ans.append(cur_list[:])
                return
            dfs(t, i + 1)
            if t - candidates[i] >= 0:
                cur_list.append(candidates[i])
                dfs(t - candidates[i], i)
                cur_list.pop()

        dfs(target, 0)
        return ans


def get_set(rl: List[List[int]]) -> Set[Tuple[int]]:
    ret = set()
    for i in rl:
        sorted(i)
        ret.add(tuple(i))
    return ret


if __name__ == '__main__':
    solution = Solution()

    result = solution.combinationSum([2, 3, 6, 7], 7)
    print(result)
    assert get_set(result) == get_set([[7], [2, 2, 3]])

    result = solution.combinationSum([2, 3, 5], 8)
    print(result)
    assert get_set(result) == get_set([[2, 2, 2, 2], [2, 3, 3], [3, 5]])

    result = solution.combinationSum([2], 1)
    print(result)
    assert get_set(result) == get_set([])

    result = solution.combinationSum([1], 1)
    print(result)
    assert get_set(result) == get_set([[1]])

    result = solution.combinationSum([1], 2)
    print(result)
    assert get_set(result) == get_set([[1, 1]])
