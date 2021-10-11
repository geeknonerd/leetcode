"""
232. 用栈实现队列
栈 设计 队列
简单


请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：

void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
 

说明：

你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
 

进阶：

你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。
 

示例：

输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]

解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

提示：

1 <= x <= 9
最多调用 100 次 push、pop、peek 和 empty
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
"""
from collections import deque


class MyQueue:

    def __init__(self):
        self.input = deque()
        self.output = deque()

    def _input_to_output(self):
        while self.input:
            self.output.append(self.input.pop())

    def _output_to_input(self):
        while self.output:
            self.input.append(self.output.pop())

    def push(self, x: int) -> None:
        self._output_to_input()
        self.input.append(x)

    def pop(self) -> int:
        self._input_to_output()
        return self.output.pop()

    def peek(self) -> int:
        self._input_to_output()
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output


def run(cmd: str, arg_list: list = [], obj: MyQueue = None):
    def init(*args):
        return MyQueue()

    return init() if cmd == 'MyQueue' else getattr(obj, cmd)(*arg_list)


def many_run(cmd_list: list):
    obj = run(cmd_list[0][0], cmd_list[0][1])
    res = [None]
    for cmd, args in cmd_list[1:]:
        res.append(run(cmd, args, obj))
    return res


if __name__ == '__main__':
    params = [("MyQueue", []), ("push", [1]), ("push", [2]), ("peek", []), ("pop", []), ("empty", [])]
    result = many_run(params)
    print(result)
    assert result == [None, None, None, 1, 1, False]
