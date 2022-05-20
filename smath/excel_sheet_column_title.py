"""
168. Excel表列名称
数学 字符串
简单


给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
 

示例 1：

输入：columnNumber = 1
输出："A"
示例 2：

输入：columnNumber = 28
输出："AB"
示例 3：

输入：columnNumber = 701
输出："ZY"
示例 4：

输入：columnNumber = 2147483647
输出："FXSHRXW"
 

提示：

1 <= columnNumber <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/excel-sheet-column-title
"""
from collections import deque


class Solution:
    chr_list = [chr(i) for i in range(65, 91)]

    def convertToTitle(self, columnNumber: int) -> str:
        chrs = deque()
        target = columnNumber - 1
        while target >= 26:
            chrs.appendleft(self.chr_list[target % 26])
            target = target // 26 - 1
        chrs.appendleft(self.chr_list[target])
        return ''.join(chrs)


if __name__ == '__main__':
    solution = Solution()

    result = solution.convertToTitle(1)
    print(result)
    assert result == 'A'

    result = solution.convertToTitle(28)
    print(result)
    assert result == 'AB'

    result = solution.convertToTitle(701)
    print(result)
    assert result == 'ZY'

    result = solution.convertToTitle(2147483647)
    print(result)
    assert result == 'FXSHRXW'

    result = solution.convertToTitle(27)
    print(result)
    assert result == 'AA'
