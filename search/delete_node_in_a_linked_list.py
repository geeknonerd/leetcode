"""
237. 删除链表中的节点
链表
简单


请编写一个函数，用于 删除单链表中某个特定节点 。在设计函数时需要注意，你无法访问链表的头节点 head ，只能直接访问 要被删除的节点 。

题目数据保证需要删除的节点 不是末尾节点 。

 

示例 1：


输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：指定链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9
示例 2：


输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：指定链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9
 

提示：

链表中节点的数目范围是 [2, 1000]
-1000 <= Node.val <= 1000
链表中每个节点的值都是 唯一 的
需要删除的节点 node 是 链表中的节点 ，且 不是末尾节点

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/delete-node-in-a-linked-list
"""


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self):
        return '{}=>{}'.format(self.val, self.next)


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        left, right = node, node.next
        while right.next:
            left.val = right.val
            left = right
            right = right.next
        left.val = right.val
        left.next = None


if __name__ == '__main__':
    solution = Solution()

    n = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
    solution.deleteNode(n.next)
    print(n)
    assert str(n) == '4=>1=>9=>None'

    n = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
    solution.deleteNode(n.next.next)
    print(n)
    assert str(n) == '4=>5=>9=>None'
