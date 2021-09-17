"""
202. 快乐数
哈希表 数学 双指针
简单


编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true ；不是，则返回 false 。

 

示例 1：

输入：19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
示例 2：

输入：n = 2
输出：false
 

提示：

1 <= n <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x: int) -> int:
            n_str = str(x)
            n_sum = 0
            for i in n_str:
                n_sum += int(i) ** 2
            return n_sum

        num_set = set()
        while n != 1 and n not in num_set:
            num_set.add(n)
            print(n)
            n = next_num(n)
        return n == 1


if __name__ == '__main__':
    solution = Solution()

    result = solution.isHappy(19)
    print(result)
    assert result is True

    result = solution.isHappy(2)
    print(result)
    assert result is False
