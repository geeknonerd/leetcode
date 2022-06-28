"""
405. 数字转换为十六进制数
位运算 回溯
简单


给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

注意:

十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
示例 1：

输入:
26

输出:
"1a"
示例 2：

输入:
-1

输出:
"ffffffff"

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/convert-a-number-to-hexadecimal
"""
from collections import deque


class Solution:
    def toHex(self, num: int) -> str:
        def int_to_hex(n: int) -> str:
            if n > 15:
                return ''
            diff = ord('0') if n < 10 else ord('a') - 10
            return chr(n + diff)
        num = 2**32 - abs(num) if num < 0 else num
        queue = deque()
        while True:
            queue.appendleft(int_to_hex(num % 16))
            quotient = num // 16
            if quotient == 0:
                break
            num = quotient
        return ''.join(queue)


if __name__ == '__main__':
    solution = Solution()

    result = solution.toHex(26)
    print(result)
    assert result == '1a'

    result = solution.toHex(0)
    print(result)
    assert result == '0'

    result = solution.toHex(-1)
    print(result)
    assert result == 'ffffffff'

