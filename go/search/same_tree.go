/*
100. 相同的树
树 深度优先搜索 广度优先搜索 二叉树
简单


给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。



示例 1：


输入：p = [1,2,3], q = [1,2,3]
输出：true
示例 2：


输入：p = [1,2], q = [1,null,2]
输出：false
示例 3：


输入：p = [1,2,1], q = [1,1,2]
输出：false


提示：

两棵树上的节点数目都在范围 [0, 100] 内
-10^4 <= Node.val <= 10^4


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/same-tree
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

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	if (p == nil && q != nil) || (p != nil && q == nil) {
		return false
	}
	if p.Val != q.Val {
		return false
	}
	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}

func main() {
	utils.Assert(isSameTree(
		&TreeNode{Val: 1,
			Left:  &TreeNode{Val: 2},
			Right: &TreeNode{Val: 3}},
		&TreeNode{Val: 1,
			Left:  &TreeNode{Val: 2},
			Right: &TreeNode{Val: 3}}), true)
	utils.Assert(isSameTree(
		&TreeNode{Val: 1,
			Left: &TreeNode{Val: 2}},
		&TreeNode{Val: 1,
			Right: &TreeNode{Val: 2}}), false)
	utils.Assert(isSameTree(
		&TreeNode{Val: 1,
			Left:  &TreeNode{Val: 2},
			Right: &TreeNode{Val: 1}},
		&TreeNode{Val: 1,
			Left:  &TreeNode{Val: 1},
			Right: &TreeNode{Val: 2}}), false)
}
