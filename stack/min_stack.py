"""
Minimum Stack

Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in  O(1)time.

Example 1:
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1

Constraints:
-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # if min_stack is not empty, only add if its smaller
        if self.min_stack and val < self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.isEmpty():
            result = self.min_stack[-1]
            item = self.stack.pop()

            # pop from min_stack if popped element equals to min_stack top
            if item == self.min_stack[-1]:
                self.min_stack.pop()

            return result
        return None

    def top(self) -> int:
        if not self.isEmpty():
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if not self.isEmpty():
            return self.min_stack[-1]
        return None

    def isEmpty(self) -> bool:
        return not self.stack