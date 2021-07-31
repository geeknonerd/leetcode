"""
21. 合并两个有序链表
递归 链表
简单


将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]
 

提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return "{}=>{}".format(self.val, self.next)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    solution = Solution()

    node1 = ListNode(1, next=ListNode(2, next=ListNode(4)))
    node2 = ListNode(1, next=ListNode(3, next=ListNode(4)))
    result = solution.mergeTwoLists(node1, node2)
    print(result)
    assert str(result) == '1=>1=>2=>3=>4=>4=>None'

    result = solution.mergeTwoLists(None, None)
    print(result)
    assert result is None

    node2 = ListNode(0)
    result = solution.mergeTwoLists(None, node2)
    print(result)
    assert str(result) == '0=>None'
