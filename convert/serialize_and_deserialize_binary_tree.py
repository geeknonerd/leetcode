"""
297. 二叉树的序列化与反序列化
树 深度优先搜索 广度优先搜索 设计 字符串 二叉树
困难


序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

 

示例 1：


输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：

输入：root = [1,2]
输出：[1,2]
 

提示：

树中结点数在范围 [0, 10^4] 内
-1000 <= Node.val <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
"""
from typing import Deque, Optional
from collections import deque


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return '{},{},{}'.format(self.val, self.left, self.right)


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.rserialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(',')
        return self.rdeserialize(deque(data_list))

    def rserialize(self, root: TreeNode, node_str: str) -> str:
        if not root:
            node_str = '{}None,'.format(node_str)
        else:
            node_str = '{}{},'.format(node_str, root.val)
            node_str = self.rserialize(root.left, node_str)
            node_str = self.rserialize(root.right, node_str)
        return node_str

    def rdeserialize(self, data_list: Deque[str]) -> Optional[TreeNode]:
        if data_list and data_list[0] == 'None':
            data_list.popleft()
            return None
        root = TreeNode(data_list[0])
        data_list.popleft()
        root.left = self.rdeserialize(data_list)
        root.right = self.rdeserialize(data_list)
        return root


if __name__ == '__main__':
    coder = Codec()

    n = TreeNode(1, left=TreeNode(2), right=TreeNode(3, left=TreeNode(4), right=TreeNode(5)))
    se = coder.serialize(n)
    dese = coder.deserialize(se)
    print(se)
    print(dese)
    assert se == '1,2,None,None,3,4,None,None,5,None,None,'
    assert str(dese) == '1,2,None,None,3,4,None,None,5,None,None'

    n = None
    se = coder.serialize(n)
    dese = coder.deserialize(se)
    print(se)
    print(dese)
    assert se == 'None,'
    assert str(dese) == 'None'

    n = TreeNode(1)
    se = coder.serialize(n)
    dese = coder.deserialize(se)
    print(se)
    print(dese)
    assert se == '1,None,None,'
    assert str(dese) == '1,None,None'

    n = TreeNode(1, left=TreeNode(2))
    se = coder.serialize(n)
    dese = coder.deserialize(se)
    print(se)
    print(dese)
    assert se == '1,2,None,None,None,'
    assert str(dese) == '1,2,None,None,None'
