/*
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
*/
package main

import (
	"fmt"
	"leetcode/go/utils"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func (n ListNode) String() string {
	return fmt.Sprintf("%v->%v", n.Val, n.Next)
}

func deleteNode(node *ListNode) {
	left := node
	right := node.Next
	for right.Next != nil {
		left.Val = right.Val
		left = right
		right = right.Next
	}
	left.Val = right.Val
	left.Next = nil
}

func main() {
	var n *ListNode
	n = &ListNode{Val: 4, Next: &ListNode{Val: 5, Next: &ListNode{Val: 1, Next: &ListNode{Val: 9}}}}
	deleteNode(n.Next)
	utils.Assert(*n, "4->1->9-><nil>")

	n = &ListNode{Val: 4, Next: &ListNode{Val: 5, Next: &ListNode{Val: 1, Next: &ListNode{Val: 9}}}}
	deleteNode(n.Next.Next)
	utils.Assert(*n, "4->5->9-><nil>")
}
