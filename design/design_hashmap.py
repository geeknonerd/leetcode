"""
706. 设计哈希映射
设计 数组 哈希表 链表 哈希函数
简单


不使用任何内建的哈希表库设计一个哈希映射（HashMap）。

实现 MyHashMap 类：

MyHashMap() 用空映射初始化对象
void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
 

示例：

输入：
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
输出：
[null, null, null, 1, -1, null, 1, null, -1]

解释：
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
 

提示：

0 <= key, value <= 106
最多调用 104 次 put、get 和 remove 方法
 

进阶：你能否不使用内置的 HashMap 库解决此问题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-hashmap
"""
from collections import deque


class Pair:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val

    def set(self, val: int):
        self.val = val


class MyHashMap:
    base = 769

    def __init__(self):
        self._list = [deque() for _ in range(self.base)]

    def put(self, key: int, value: int) -> None:
        cur_list = self._list[self.hash(key)]
        for o in cur_list:
            if o.key == key:
                o.set(value)
                return
        cur_list.append(Pair(key, value))

    def get(self, key: int) -> int:
        for o in self._list[self.hash(key)]:
            if o.key == key:
                return o.val
        return -1

    def remove(self, key: int) -> None:
        cur_list = self._list[self.hash(key)]
        for i in range(len(cur_list)):
            if cur_list[i].key == key:
                del cur_list[i]
                break

    def hash(self, key: int):
        return key % self.base


if __name__ == '__main__':
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    assert obj.get(1) == 1
    assert obj.get(3) == -1
    obj.put(2, 1)
    assert obj.get(2) == 1
    obj.remove(2)
    assert obj.get(2) == -1
