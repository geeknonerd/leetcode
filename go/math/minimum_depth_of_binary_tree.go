/*
111. 二叉树的最小深度
树 深度优先搜索 广度优先搜索 二叉树
简单


给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。



示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：2
示例 2：

输入：root = [2,null,3,null,4,null,5,null,6]
输出：5


提示：

树中节点数的范围在 [0, 10^5] 内
-1000 <= Node.val <= 1000


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-depth-of-binary-tree
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

var maxDefaultVal = 100001

func isLeaf(node *TreeNode) bool {
	if node != nil && node.Left == nil && node.Right == nil {
		return true
	}
	return false
}

func minDepthNilMax(root *TreeNode) int {
	if root == nil {
		return maxDefaultVal
	}
	if isLeaf(root) {
		return 1
	}
	leftVal := minDepthNilMax(root.Left)
	rightVal := minDepthNilMax(root.Right)
	if leftVal > rightVal {
		return rightVal + 1
	}
	return leftVal + 1
}

func minDepth(root *TreeNode) int {
	res := minDepthNilMax(root)
	if res >= maxDefaultVal {
		return 0
	}
	return res
}

func main() {
	utils.Assert(minDepth(
		&TreeNode{Val: 3,
			Left: &TreeNode{Val: 9},
			Right: &TreeNode{Val: 20,
				Left:  &TreeNode{Val: 15},
				Right: &TreeNode{Val: 7}}}), 2)
	utils.Assert(minDepth(
		&TreeNode{Val: 2,
			Right: &TreeNode{Val: 3,
				Right: &TreeNode{Val: 4,
					Right: &TreeNode{Val: 5,
						Right: &TreeNode{Val: 6}}}}}), 5)
	utils.Assert(minDepth(nil), 0)
}
