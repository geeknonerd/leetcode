"""
143. 重排链表
栈 递归 链表 双指针
中等


给定一个单链表 L 的头节点 head ，单链表 L 表示为：

 L0 → L1 → … → Ln-1 → Ln 
请将其重新排列后变为：

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例 1:



输入: head = [1,2,3,4]
输出: [1,4,2,3]
示例 2:



输入: head = [1,2,3,4,5]
输出: [1,5,2,4,3]
 

提示：

链表的长度范围为 [1, 5 * 104]
1 <= node.val <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-list
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '{}{}'.format(self.val, ',{}'.format(self.next) if self.next else '')


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        vec = []
        cur = head
        while cur:
            vec.append(cur)
            cur = cur.next
        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1
        vec[i].next = None


if __name__ == '__main__':
    solution = Solution()

    result = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4))))
    solution.reorderList(result)
    print(result)
    assert str(result) == '1,4,2,3'

    result = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
    solution.reorderList(result)
    print(result)
    assert str(result) == '1,5,2,4,3'
