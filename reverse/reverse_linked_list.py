"""
206. 反转链表
递归 链表
简单


给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
 

示例 1：


输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：


输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]
 

提示：

链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000
 

进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return "{}=>{}".format(self.val, self.next)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_node


if __name__ == '__main__':
    solution = Solution()

    node = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
    result = solution.reverseList(node)
    print(result)
    assert str(result) == '5=>4=>3=>2=>1=>None'

    node = ListNode(1, next=ListNode(2))
    result = solution.reverseList(node)
    print(result)
    assert str(result) == '2=>1=>None'

    result = solution.reverseList(None)
    print(result)
    assert result is None
