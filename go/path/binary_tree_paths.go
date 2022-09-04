/*
257. 二叉树的所有路径
树 深度优先搜索 字符串 回溯 二叉树
简单


给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

叶子节点 是指没有子节点的节点。


示例 1：


输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]
示例 2：

输入：root = [1]
输出：["1"]


提示：

树中节点的数目在范围 [1, 100] 内
-100 <= Node.val <= 100

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-tree-paths
*/
package main

import (
	"leetcode/go/utils"
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dfs(node *TreeNode, stack *[]string, paths *[]string) {
	if node == nil {
		return
	}
	*stack = append(*stack, strconv.Itoa(node.Val))
	size := len(*stack)
	if node.Left == nil && node.Right == nil {
		builder := strings.Builder{}
		for i, v := range *stack {
			builder.WriteString(v)
			if i == size-1 {
				break
			}
			builder.WriteString("->")
		}
		*paths = append(*paths, builder.String())
		*stack = (*stack)[:size-1]
		return
	}
	dfs(node.Left, stack, paths)
	dfs(node.Right, stack, paths)
	*stack = (*stack)[:size-1]
}

func binaryTreePaths(root *TreeNode) []string {
	var ret []string
	var stack []string
	dfs(root, &stack, &ret)
	return ret
}

func main() {
	n := &TreeNode{Val: 1, Left: &TreeNode{Val: 2, Right: &TreeNode{Val: 5}}, Right: &TreeNode{Val: 3}}
	utils.Assert(binaryTreePaths(n), []string{"1->2->5", "1->3"})

	n = &TreeNode{Val: 1}
	utils.Assert(binaryTreePaths(n), []string{"1"})
}
