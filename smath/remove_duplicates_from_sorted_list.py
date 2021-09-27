"""
83. 删除排序链表中的重复元素
链表
简单


存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。

返回同样按升序排列的结果链表。

 

示例 1：


输入：head = [1,1,2]
输出：[1,2]
示例 2：


输入：head = [1,1,2,3,3]
输出：[1,2,3]
 

提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '{}{}'.format(self.val, ',{}'.format(self.next) if self.next else '')


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre_n = head
        next_n = head.next
        while next_n:
            if pre_n.val == next_n.val:
                next_n = next_n.next
                pre_n.next = next_n
            else:
                pre_n = next_n
                next_n = next_n.next
        return head


if __name__ == '__main__':
    solution = Solution()

    node = ListNode(1, ListNode(1, ListNode(2)))
    result = solution.deleteDuplicates(node)
    print(result)
    assert str(result) == '1,2'

    node = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    result = solution.deleteDuplicates(node)
    print(result)
    assert str(result) == '1,2,3'
