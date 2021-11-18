"""
24. 两两交换链表中的节点
递归 链表
中等


给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]
 

提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100
 

进阶：你能在不修改链表节点值的情况下解决这个问题吗?（也就是说，仅修改节点本身。）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pass


if __name__ == '__main__':
    solution = Solution()

    node = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4))))
    result = solution.swapPairs(node)
    print(result)
    assert str(result) == '2,1,4,3'

    node = None
    result = solution.swapPairs(node)
    print(result)
    assert str(result) == ''

    node = ListNode(1)
    result = solution.swapPairs(node)
    print(result)
    assert str(result) == '1'
