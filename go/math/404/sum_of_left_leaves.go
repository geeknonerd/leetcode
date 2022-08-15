/*
404. 左叶子之和
树 深度优先搜索 广度优先搜索 二叉树
简单


给定二叉树的根节点 root ，返回所有左叶子之和。



示例 1：



输入: root = [3,9,20,null,null,15,7]
输出: 24
解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
示例 2:

输入: root = [1]
输出: 0


提示:

节点数在 [1, 1000] 范围内
-1000 <= Node.val <= 1000


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sum-of-left-leaves
*/
package main

import (
	"leetcode/go/utils"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recursion(isLeft bool, node *TreeNode) int {
	sum := 0
	if node == nil {
		return sum
	}
	if isLeft && node.Left == nil && node.Right == nil {
		sum += node.Val
		return sum
	}
	sum += recursion(true, node.Left)
	sum += recursion(false, node.Right)
	return sum
}

func sumOfLeftLeaves(root *TreeNode) int {
	return recursion(false, root)
}

func main() {
	node := TreeNode{Val: 3, Left: &TreeNode{Val: 9}, Right: &TreeNode{Val: 20, Left: &TreeNode{Val: 15}, Right: &TreeNode{Val: 7}}}
	utils.Assert(sumOfLeftLeaves(&node), 24)

	node = TreeNode{Val: 1}
	utils.Assert(sumOfLeftLeaves(&node), 0)
}
