"""
9. 回文数
数学
简单


给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。
 

示例 1：

输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
 

提示：

-2^31 <= x <= 2^31 - 1
 

进阶：你能不将整数转为字符串来解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
"""
from collections import deque


class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = deque()
        if x < 0:
            return False
        while x // 10 > 0:
            nums.append(x % 10)
            x //= 10
        nums.append(x)
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    solution = Solution()

    result = solution.isPalindrome(121)
    print(result)
    assert result is True

    result = solution.isPalindrome(-121)
    print(result)
    assert result is False

    result = solution.isPalindrome(10)
    print(result)
    assert result is False
