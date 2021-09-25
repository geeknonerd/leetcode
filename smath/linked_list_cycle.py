"""
141. 环形链表
哈希表 链表 双指针
简单


给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。

 

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

 

示例 1：



输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：



输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：



输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
 

提示：

链表中节点的数目范围是 [0, 104]
-105 <= Node.val <= 105
pos 为 -1 或者链表中的一个 有效索引 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
"""


# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return 'Node({})'.format(self.val)


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        while slow and slow.next and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def get_link_node(nums: List[int], pos: int) -> ListNode:
    node_list = [ListNode(i) for i in nums]
    for i in range(len(node_list)-1):
        node_list[i].next = node_list[i+1]
    if pos >= 0:
        node_list[-1].next = node_list[pos]
    return node_list[0]


if __name__ == '__main__':
    solution = Solution()

    target = get_link_node([3,2,0,-4], 1)
    result = solution.hasCycle(target)
    print(result)
    assert result is True

    target = get_link_node([1,2], 0)
    result = solution.hasCycle(target)
    print(result)
    assert result is True

    target = get_link_node([1], -1)
    result = solution.hasCycle(target)
    print(result)
    assert result is False
