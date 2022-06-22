"""
374. 猜数字大小
二分查找 交互
简单


猜数字游戏的规则如下：

每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：

-1：我选出的数字比你猜的数字小 pick < num
1：我选出的数字比你猜的数字大 pick > num
0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
返回我选出的数字。

 

示例 1：

输入：n = 10, pick = 6
输出：6
示例 2：

输入：n = 1, pick = 1
输出：1
示例 3：

输入：n = 2, pick = 1
输出：1
示例 4：

输入：n = 2, pick = 2
输出：2
 

提示：

1 <= n <= 231 - 1
1 <= pick <= n

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/guess-number-higher-or-lower
"""
pick = 0


def guess(num: int) -> int:
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if guess(mid) <= 0:
                right = mid  # 答案在区间 [left, mid] 中
            else:
                left = mid + 1  # 答案在区间 [mid+1, right] 中
        # 此时有 left == right，区间缩为一个点，即为答案
        return left


if __name__ == '__main__':
    solution = Solution()

    pick = 6
    result = solution.guessNumber(10)
    print(result)
    assert result == 6

    pick = 1
    result = solution.guessNumber(1)
    print(result)
    assert result == 1

    pick = 1
    result = solution.guessNumber(2)
    print(result)
    assert result == 1

    pick = 2
    result = solution.guessNumber(2)
    print(result)
    assert result == 2
