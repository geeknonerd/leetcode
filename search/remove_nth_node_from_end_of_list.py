"""
19. 删除链表的倒数第 N 个结点
链表 双指针
中等


给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？

 

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]
 

提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
"""

# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return '({}) -> {}'.format(self.val, self.next)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> Optional[ListNode]:
        empty_head = ListNode(0, head)
        slow = fast = empty_head
        while fast:
            fast = fast.next
            if n < 0:
                slow = slow.next
            if n >= 0:
                n -= 1
        rm_node = slow.next
        slow.next = rm_node.next
        rm_node.next = None
        return empty_head.next


def array_to_link(nums: List[int]) -> Optional[ListNode]:
    if not nums:
        return None
    nodes = []
    for i in nums:
        nodes.append(ListNode(i))
    for j in range(len(nodes) - 1):
        nodes[j].next = nodes[j + 1]
    return nodes[0]


def link_to_array(node: ListNode) -> List[int]:
    cur = node
    nums = []
    while cur:
        nums.append(cur.val)
        cur = cur.next
    return nums


if __name__ == '__main__':
    # print(array_to_link([1, 2, 3, 4, 5]))
    # print(link_to_array(array_to_link([1, 2, 3, 4, 5])))

    solution = Solution()

    head_node = solution.removeNthFromEnd(array_to_link([1, 2, 3, 4, 5]), 2)
    print(head_node)
    result = link_to_array(head_node)
    assert result == [1, 2, 3, 5]

    head_node = solution.removeNthFromEnd(array_to_link([1]), 1)
    print(head_node)
    result = link_to_array(head_node)
    assert result == []

    head_node = solution.removeNthFromEnd(array_to_link([1, 2]), 1)
    print(head_node)
    result = link_to_array(head_node)
    assert result == [1]
