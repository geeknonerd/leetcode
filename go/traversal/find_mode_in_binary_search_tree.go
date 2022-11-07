/*
501. 二叉搜索树中的众数
树 深度优先搜素 二叉搜素树 二叉树
简单


给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。

如果树中有不止一个众数，可以按 任意顺序 返回。

假定 BST 满足如下定义：

结点左子树中所含节点的值 小于等于 当前节点的值
结点右子树中所含节点的值 大于等于 当前节点的值
左子树和右子树都是二叉搜索树


示例 1：


输入：root = [1,null,2,2]
输出：[2]
示例 2：

输入：root = [0]
输出：[0]


提示：

树中节点的数目在范围 [1, 104] 内
-10^5 <= Node.val <= 10^5


进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-mode-in-binary-search-tree
*/
package main

import (
	"leetcode/go/utils"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dfs(numCnt map[int]int, node *TreeNode) {
	if node == nil {
		return
	}
	if _, ok := numCnt[node.Val]; ok {
		numCnt[node.Val]++
	} else {
		numCnt[node.Val] = 1
	}
	dfs(numCnt, node.Left)
	dfs(numCnt, node.Right)

}

func findMode(root *TreeNode) []int {
	numCnt := make(map[int]int)
	dfs(numCnt, root)
	var res []int
	maxVal := -int(math.Pow(float64(10), float64(5))) - 1
	for k, v := range numCnt {
		if v > maxVal {
			res = []int{k}
			maxVal = v
		} else if v == maxVal {
			res = append(res, k)
		}
	}
	return res
}

func main() {
	utils.Assert(findMode(&TreeNode{Val: 1, Right: &TreeNode{Val: 2, Left: &TreeNode{Val: 2}}}), []int{2})
	utils.Assert(findMode(&TreeNode{Val: 1, Right: &TreeNode{Val: 2}}), []int{1, 2})
	utils.Assert(findMode(&TreeNode{Val: 0}), []int{0})
}
