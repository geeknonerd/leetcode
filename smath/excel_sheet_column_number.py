"""
171. Excel 表列序号
数学 字符串
简单


给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
 

示例 1:

输入: columnTitle = "A"
输出: 1
示例 2:

输入: columnTitle = "AB"
输出: 28
示例 3:

输入: columnTitle = "ZY"
输出: 701
 

提示：

1 <= columnTitle.length <= 7
columnTitle 仅由大写英文组成
columnTitle 在范围 ["A", "FXSHRXW"] 内

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/excel-sheet-column-number
"""
from collections import OrderedDict


class Solution:
    def __init__(self):
        self.chr_dict = OrderedDict()
        for i in range(65, 91):
            self.chr_dict[chr(i)] = i - 64

    def titleToNumber(self, columnTitle: str) -> int:
        sum = 0
        for i in range(1, len(columnTitle)+1):
            sum += self.chr_dict[columnTitle[-i]] * 26 ** (i-1)
        return sum


if __name__ == '__main__':
    solution = Solution()

    result = solution.titleToNumber("A")
    print(result)
    assert result == 1

    result = solution.titleToNumber("AB")
    print(result)
    assert result == 28

    result = solution.titleToNumber("ZY")
    print(result)
    assert result == 701
