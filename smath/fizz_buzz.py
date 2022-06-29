"""
412. Fizz Buzz
数学 字符串 模拟
简单


给你一个整数 n ，找出从 1 到 n 各个整数的 Fizz Buzz 表示，并用字符串数组 answer（下标从 1 开始）返回结果，其中：

answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
answer[i] == "Fizz" 如果 i 是 3 的倍数。
answer[i] == "Buzz" 如果 i 是 5 的倍数。
answer[i] == i （以字符串形式）如果上述条件全不满足。
 

示例 1：

输入：n = 3
输出：["1","2","Fizz"]
示例 2：

输入：n = 5
输出：["1","2","Fizz","4","Buzz"]
示例 3：

输入：n = 15
输出：["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

提示：

1 <= n <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/fizz-buzz
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            is_treble = i % 3 == 0
            is_quintuple = i % 5 == 0
            if is_treble and is_quintuple:
                tmp = 'FizzBuzz'
            elif is_treble and not is_quintuple:
                tmp = 'Fizz'
            elif not is_treble and is_quintuple:
                tmp = 'Buzz'
            else:
                tmp = str(i)
            res.append(tmp)
        return res


if __name__ == '__main__':
    solution = Solution()

    result = solution.fizzBuzz(3)
    print(result)
    assert result == ["1", "2", "Fizz"]

    result = solution.fizzBuzz(5)
    print(result)
    assert result == ["1", "2", "Fizz", "4", "Buzz"]

    result = solution.fizzBuzz(15)
    print(result)
    assert result == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14",
                      "FizzBuzz"]
