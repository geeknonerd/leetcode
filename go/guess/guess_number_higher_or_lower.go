/*
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
*/
package main

import (
	"leetcode/go/utils"
)

var pick int

func guess(num int) int {
	if pick < num {
		return -1
	} else if pick > num {
		return 1
	}
	return 0
}

func guessNumber(n int) int {
	left := 0
	right := n
	for left < right {
		mid := (left + right) / 2
		if guess(mid) == 0 {
			return mid
		} else if guess(mid) < 0 {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return left
}

func main() {
	pick = 6
	utils.Assert(guessNumber(10), 6)
	pick = 1
	utils.Assert(guessNumber(1), 1)
	pick = 1
	utils.Assert(guessNumber(2), 1)
	pick = 2
	utils.Assert(guessNumber(2), 2)
}
