"""
117. 填充每个节点的下一个右侧节点指针 II
树 深度优先搜索 广度优先搜索 二叉树
中等


给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

 

进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 

示例：



输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。
 

提示：

树中的节点数小于 6000
-100 <= node.val <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii
"""
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self) -> str:
        return '[{},{},{},{}]'.format(self.val, self.next.val if self.next else '#', self.left, self.right)


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque([root])
        while queue:
            size = len(queue)
            tmp = queue[0]
            for i in range(1, size):
                tmp.next = queue[i]
                tmp = queue[i]
            for _ in range(size):
                tmp = queue.popleft()
                if not tmp:
                    continue
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
        return root


if __name__ == '__main__':
    solution = Solution()

    node = Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, right=Node(7)))
    result = solution.connect(node)
    print(result)
    assert str(result) == '[1,#,[2,3,[4,5,None,None],[5,7,None,None]],[3,#,None,[7,#,None,None]]]'

    node = Node()
    result = solution.connect(node)
    print(result)
    assert str(result) == '[0,#,None,None]'
