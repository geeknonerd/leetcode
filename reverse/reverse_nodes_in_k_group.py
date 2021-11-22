"""
25. K 个一组翻转链表
递归 链表
困难


给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：

你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
 

示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
示例 2：


输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
示例 3：

输入：head = [1,2,3,4,5], k = 1
输出：[1,2,3,4,5]
示例 4：

输入：head = [1], k = 1
输出：[1]
提示：

列表中节点的数量在范围 sz 内
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '{},{}'.format(self.val, self.next)


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(h: ListNode, t: ListNode):
            prev = t.next
            p = h
            while prev != t:
                tmp = p.next
                p.next = prev
                prev = p
                p = tmp
            return t, h

        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = reverse(head, tail)
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return hair.next


if __name__ == '__main__':
    solution = Solution()

    n = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
    result = solution.reverseKGroup(n, 2)
    print(result)
    assert str(result) == '2,1,4,3,5,None'

    n = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
    result = solution.reverseKGroup(n, 3)
    print(result)
    assert str(result) == '3,2,1,4,5,None'

    n = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
    result = solution.reverseKGroup(n, 1)
    print(result)
    assert str(result) == '1,2,3,4,5,None'

    n = ListNode(1)
    result = solution.reverseKGroup(n, 1)
    print(result)
    assert str(result) == '1,None'
