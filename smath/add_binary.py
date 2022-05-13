"""
67. 二进制求和
位运算 数学 字符串 模拟
简单


给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-binary
"""
from collections import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        def get_num(s, size, index):
            if -size <= index < size:
                return 1 if s[index] == '1' else 0
            return 0

        a_size = len(a)
        b_size = len(b)
        carry_num = 0
        ret = deque()
        for i in range(1, max(a_size, b_size) + 1):
            a_num = get_num(a, a_size, -i)
            b_num = get_num(b, b_size, -i)
            sum_num = a_num + b_num + carry_num
            ret.appendleft(str(sum_num % 2))
            carry_num = sum_num // 2
        if carry_num > 0:
            ret.appendleft(str(carry_num))
        return ''.join(ret)


if __name__ == '__main__':
    solution = Solution()

    result = solution.addBinary("11", "1")
    print(result)
    assert result == "100"

    result = solution.addBinary("1010", "1011")
    print(result)
    assert result == "10101"
