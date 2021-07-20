"""
876. 链表的中间结点
链表 双指针
简单


给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

 

示例 1：

输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
 

提示：

给定链表的结点数介于 1 和 100 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/middle-of-the-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return 'LN({}){{{}}}'.format(self.val, self.next)


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        is_run = True
        while is_run:
            if not slow.next:
                break
            slow = slow.next
            for _ in range(2):
                if not fast.next:
                    is_run = False
                    break
                fast = fast.next
            if not fast.next:
                is_run = False
        return slow


def gen_list_node(nums: List[int]) -> ListNode:
    head = ListNode(nums[0])
    pre = head
    for i in nums[1:]:
        cur = ListNode(i)
        pre.next = cur
        pre = cur
    return head


if __name__ == '__main__':
    solution = Solution()

    # print(gen_list_node([1, 2, 3, 4, 5]))
    ans = solution.middleNode(gen_list_node([1, 2, 3, 4, 5]))
    print(ans.val)
    assert ans.val == 3

    ans = solution.middleNode(gen_list_node([1, 2, 3, 4, 5, 6]))
    print(ans.val)
    assert ans.val == 4

    ans = solution.middleNode(gen_list_node([1]))
    print(ans.val)
    assert ans.val == 1
