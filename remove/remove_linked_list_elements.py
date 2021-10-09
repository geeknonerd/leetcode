"""
203. 移除链表元素
递归 链表
简单


给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
 

示例 1：


输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
示例 2：

输入：head = [], val = 1
输出：[]
示例 3：

输入：head = [7,7,7,7], val = 7
输出：[]
 

提示：

列表中的节点数目在范围 [0, 10^4] 内
1 <= Node.val <= 50
0 <= val <= 50

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-linked-list-elements
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '{}{}'.format(self.val, ',{}'.format(self.next) if self.next else '')


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        pre_head = ListNode(next=head)
        pre_n = pre_head
        next_n = pre_head.next
        while next_n:
            if next_n.val == val:
                next_n = next_n.next
                pre_n.next = next_n
            else:
                next_n = next_n.next
                pre_n = pre_n.next
        return pre_head.next


if __name__ == '__main__':
    solution = Solution()

    n = ListNode(1, next=ListNode(2, next=ListNode(6, next=ListNode(
        3, next=ListNode(4, next=ListNode(5, next=ListNode(6)))))))
    result = solution.removeElements(n, 6)
    print(result)
    assert str(result) == '1,2,3,4,5'

    result = solution.removeElements(None, 1)
    print(result)
    assert result is None

    n = ListNode(7, next=ListNode(7, next=ListNode(7, next=ListNode(7))))
    result = solution.removeElements(n, 7)
    print(result)
    assert result is None
