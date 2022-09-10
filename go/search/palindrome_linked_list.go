/*
234. 回文链表
栈 递归 链表 双指针
简单


给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。



示例 1：


输入：head = [1,2,2,1]
输出：true
示例 2：


输入：head = [1,2]
输出：false


提示：

链表中节点数目在范围[1, 10^5] 内
0 <= Node.val <= 9


进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/palindrome-linked-list
*/
package main

import (
	"leetcode/go/utils"
)

//func isPalindrome(head *ListNode) bool {
//	frontPointer := head
//	var recursivelyCheck func(*ListNode) bool
//	recursivelyCheck = func(curNode *ListNode) bool {
//		if curNode != nil {
//			if !recursivelyCheck(curNode.Next) {
//				return false
//			}
//			if curNode.Val != frontPointer.Val {
//				return false
//			}
//			frontPointer = frontPointer.Next
//		}
//		return true
//	}
//	return recursivelyCheck(head)
//}

type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	frontPointer := head
	var recursivelyCheck func(*ListNode) bool
	recursivelyCheck = func(curNode *ListNode) bool {
		if curNode != nil {
			if !recursivelyCheck(curNode.Next) {
				return false
			}
			if curNode.Val != frontPointer.Val {
				return false
			}
			frontPointer = frontPointer.Next
		}
		return true
	}
	return recursivelyCheck(head)
}

func main() {
	var n *ListNode

	n = &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 2, Next: &ListNode{Val: 1}}}}
	utils.Assert(isPalindrome(n), true)

	n = &ListNode{Val: 1, Next: &ListNode{Val: 2}}
	utils.Assert(isPalindrome(n), false)
}
