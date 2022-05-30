"""
234. 回文链表
栈 递归 链表 双指针
简单


给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

 

示例 1：


输入：head = [1,2,2,1]
输出：true
示例 2：


输入：head = [1,2]
输出：false
 

提示：

链表中节点数目在范围[1, 10^5] 内
0 <= Node.val <= 9
 

进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/palindrome-linked-list
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def recursively_check(cur_node: ListNode) -> bool:
            nonlocal front
            if cur_node is not None:
                if not recursively_check(cur_node.next):
                    return False
                if front.val != cur_node.val:
                    return False
                front = front.next
            return True
        front = head
        return recursively_check(head)


if __name__ == '__main__':
    solution = Solution()

    n = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    result = solution.isPalindrome(n)
    print(result)
    assert result is True

    n = ListNode(1, ListNode(2))
    result = solution.isPalindrome(n)
    print(result)
    assert result is False
