/*
110. 平衡二叉树
树 深度优先搜索 二叉树
简单


给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。



示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：true
示例 2：


输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
示例 3：

输入：root = []
输出：true


提示：

树中的节点数在范围 [0, 5000] 内
-10^4 <= Node.val <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/balanced-binary-tree
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

func getTreeHigh(node *TreeNode) int {
	if node == nil {
		return 0
	}
	leftHigh := getTreeHigh(node.Left)
	rightHigh := getTreeHigh(node.Right)
	res := 0
	if leftHigh > rightHigh {
		res = leftHigh + 1
	} else {
		res = rightHigh + 1
	}
	return res
}

func isBalanced(root *TreeNode) bool {
	if root == nil {
		return true
	}
	highDiff := getTreeHigh(root.Left) - getTreeHigh(root.Right)
	if highDiff > -2 && highDiff < 2 && isBalanced(root.Left) && isBalanced(root.Right) {
		return true
	}
	return false
}

func main() {
	utils.Assert(isBalanced(
		&TreeNode{Val: 3,
			Left: &TreeNode{Val: 9},
			Right: &TreeNode{Val: 20,
				Left:  &TreeNode{Val: 15},
				Right: &TreeNode{Val: 7}}}), true)
	utils.Assert(isBalanced(
		&TreeNode{Val: 1,
			Left: &TreeNode{Val: 2,
				Left: &TreeNode{Val: 3,
					Left: &TreeNode{Val: 4}, Right: &TreeNode{Val: 4}},
				Right: &TreeNode{Val: 3}},
			Right: &TreeNode{Val: 2}}), false)
	utils.Assert(isBalanced(nil), true)
}
