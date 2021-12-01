"""
347. 前 K 个高频元素
数组 哈希表 分治 桶排序 计数 快速选择 排序 堆（优先队列）
中等


给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

 

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
 

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_cnt_dict = defaultdict(int)
        for i in nums:
            num_cnt_dict[i] += 1
        q = []
        for n, c in num_cnt_dict.items():
            heapq.heappush(q, (-c, n))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(q)[1])
        return res


if __name__ == '__main__':
    solution = Solution()

    result = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    print(result)
    assert result == [1, 2]

    result = solution.topKFrequent([1], 1)
    print(result)
    assert result == [1]

    result = solution.topKFrequent([3, 0, 1, 0], 1)
    print(result)
    assert result == [0]
