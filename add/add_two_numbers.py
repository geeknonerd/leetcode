"""
2. 两数相加
递归 链表 数学
中等


给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
 

提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '{}{}'.format(self.val, ',{}'.format(self.next) if self.next else '')


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode()
        cur = root
        cur1 = l1
        cur2 = l2
        add_v = 0
        while cur1 or cur2 or add_v:
            cur1_val = cur1.val if cur1 else 0
            cur2_val = cur2.val if cur2 else 0
            val = cur1_val + cur2_val + add_v
            cur.next = ListNode(val % 10)
            add_v = val // 10
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            cur = cur.next
        return root.next


if __name__ == '__main__':
    solution = Solution()

    n1 = ListNode(2, next=ListNode(4, next=ListNode(3)))
    n2 = ListNode(5, next=ListNode(6, next=ListNode(4)))
    result = solution.addTwoNumbers(n1, n2)
    print(result)
    assert str(result) == '7,0,8'

    n1 = ListNode()
    n2 = ListNode()
    result = solution.addTwoNumbers(n1, n2)
    print(result)
    assert str(result) == '0'

    n1 = ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(
        9, next=ListNode(9, next=ListNode(9, next=ListNode(9)))))))
    n2 = ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9))))
    result = solution.addTwoNumbers(n1, n2)
    print(result)
    assert str(result) == '8,9,9,9,0,0,0,1'
