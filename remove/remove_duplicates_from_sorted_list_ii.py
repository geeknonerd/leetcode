"""
82. 删除排序链表中的重复元素 II
链表 双指针
中等


存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。

返回同样按升序排列的结果链表。

 

示例 1：


输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
示例 2：


输入：head = [1,1,1,2,3]
输出：[2,3]
 

提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
"""


# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return '{} -> {}'.format(self.val, self.next)


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        root = ListNode(0, head)
        cur = root
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return root.next


def array_to_linked_list(nums: List[int]) -> ListNode:
    if not nums:
        return ListNode()
    head = ListNode(nums[0])
    cur = head
    for i in nums[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head


def linked_list_to_array(head: ListNode) -> List[int]:
    cur = head
    nums = []
    while cur:
        nums.append(cur.val)
        cur = cur.next
    return nums


if __name__ == '__main__':
    solution = Solution()

    # print(array_to_linked_list([1, 2, 3, 3, 4, 4, 5]))
    # print(linked_list_to_array(array_to_linked_list([1, 2, 3, 3, 4, 4, 5])))

    result = solution.deleteDuplicates(array_to_linked_list([1, 2, 3, 3, 4, 4, 5]))
    print(linked_list_to_array(result))
    assert linked_list_to_array(result) == [1, 2, 5]

    result = solution.deleteDuplicates(array_to_linked_list([1, 1, 1, 2, 3]))
    print(linked_list_to_array(result))
    assert linked_list_to_array(result) == [2, 3]
