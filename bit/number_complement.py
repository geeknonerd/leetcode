"""
476. 数字的补数
位运算
简单


对整数的二进制表示取反（0 变 1 ，1 变 0）后，再转换为十进制表示，可以得到这个整数的补数。

例如，整数 5 的二进制表示是 "101" ，取反后得到 "010" ，再转回十进制表示得到补数 2 。
给你一个整数 num ，输出它的补数。

 

示例 1：

输入：num = 5
输出：2
解释：5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
示例 2：

输入：num = 1
输出：0
解释：1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
 

提示：

1 <= num < 2^31
 

注意：本题与 1009 https://leetcode-cn.com/problems/complement-of-base-10-integer/ 相同

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/number-complement
"""


class Solution:
    def findComplement(self, num: int) -> int:
        high = 0
        for i in range(1, 31):
            if num >= (1 << i):
                high = i
            else:
                break
        mask = (1 << (high+1)) - 1
        return num ^ mask


if __name__ == '__main__':
    solution = Solution()

    result = solution.findComplement(5)
    print(result)
    assert result == 2

    result = solution.findComplement(1)
    print(result)
    assert result == 0
