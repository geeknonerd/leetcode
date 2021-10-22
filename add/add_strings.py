"""
415. 字符串相加
数学 字符串 模拟
简单


给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。

 

示例 1：

输入：num1 = "11", num2 = "123"
输出："134"
示例 2：

输入：num1 = "456", num2 = "77"
输出："533"
示例 3：

输入：num1 = "0", num2 = "0"
输出："0"
 

 

提示：

1 <= num1.length, num2.length <= 104
num1 和num2 都只包含数字 0-9
num1 和num2 都不包含任何前导零

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        add = 0
        ord_0 = ord('0')
        ans = []
        while i >= 0 or j >= 0 or add != 0:
            x = ord(num1[i]) - ord_0 if i >= 0 else 0
            y = ord(num2[j]) - ord_0 if j >= 0 else 0
            res = x + y + add
            ans.append(str(res % 10))
            add = res // 10
            i -= 1
            j -= 1
        return ''.join(reversed(ans))


if __name__ == '__main__':
    solution = Solution()

    result = solution.addStrings("11",  "123")
    print(result)
    assert result == '134'

    result = solution.addStrings("456",  "77")
    print(result)
    assert result == '533'

    result = solution.addStrings("0", "0")
    print(result)
    assert result == '0'
