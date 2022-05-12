"""
66. 加一
数组 数学
简单


给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

 

示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：

输入：digits = [0]
输出：[1]
 

提示：

1 <= digits.length <= 100
0 <= digits[i] <= 9

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/plus-one
"""
from typing import List
from collections import deque


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add_val = 1
        new_digits = deque(digits)
        for i in range(len(new_digits)-1, -1, -1):
            val = new_digits[i] + add_val
            if add_val > 0:
                add_val -= 1
            if val > 9:
                add_val = val // 10
                val = val % 10
            new_digits[i] = val
        if add_val > 0:
            new_digits.appendleft(add_val)
        return list(new_digits)


if __name__ == '__main__':
    solution = Solution()

    result = solution.plusOne([1, 2, 3])
    print(result)
    assert result == [1, 2, 4]

    result = solution.plusOne([4, 3, 2, 1])
    print(result)
    assert result == [4, 3, 2, 2]

    result = solution.plusOne([0])
    print(result)
    assert result == [1]

    result = solution.plusOne([1, 9, 9])
    print(result)
    assert result == [2, 0, 0]

    result = solution.plusOne([9, 9])
    print(result)
    assert result == [1, 0, 0]
