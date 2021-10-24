"""
43. 字符串相乘
数学 字符串 模拟
中等


给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len_1, len_2 = len(num1), len(num2)
        ord_0 = ord('0')
        num1_list = [ord(num1[i]) - ord_0 for i in range(len_1 - 1, -1, -1)]
        num2_list = [ord(num2[i]) - ord_0 for i in range(len_2 - 1, -1, -1)]
        res = 0
        for i in range(len_1):
            n1 = num1_list[i] * 10 ** i
            for j in range(len_2):
                n2 = num2_list[j] * 10 ** j
                res += n1 * n2
        return str(res)


if __name__ == '__main__':
    solution = Solution()

    result = solution.multiply("2", "3")
    print(result)
    assert result == "6"

    result = solution.multiply("123", "456")
    print(result)
    assert result == "56088"
