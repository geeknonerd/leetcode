"""
707. 设计链表
设计 链表
中等


设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
 

示例：

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3
 

提示：

所有val值都在 [1, 1000] 之内。
操作次数将在  [1, 1000] 之内。
请不要使用内置的 LinkedList 库。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-linked-list
"""


class Node:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class MyLinkedList:

    def __init__(self):
        self.head = Node()

    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        cur = Node(val)
        cur.next = self.head.next if self.head.next else None
        self.head.next = cur

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            self.addAtHead(val)
            return
        cur = self.head
        i = 0
        while cur:
            if i == index:
                new_node = Node(val)
                new_node.next = cur.next
                cur.next = new_node
                break
            cur = cur.next
            i += 1

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        i = 0
        while cur:
            if i == index:
                cur.next = cur.next.next if cur.next else None
                break
            cur = cur.next
            i += 1


if __name__ == '__main__':
    solution = MyLinkedList()

    solution.addAtHead(1)
    solution.addAtTail(3)
    solution.addAtIndex(1, 2)
    print(solution.get(1))
    assert solution.get(1) == 2
    solution.deleteAtIndex(1)
    print(solution.get(1))
    assert solution.get(1) == 3
