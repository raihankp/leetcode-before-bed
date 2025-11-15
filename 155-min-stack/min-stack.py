class MinStack:
    # Bruteforce:
    # To get the minimum element, we could just loop through the stack array
    # But time complexity would be O(n)

    # Better solution:
    # Create 2 stack where 1 is for the stack and 1 is for the minimum value for each node in the stack
    # Like for example, when we push a digit, there are 2 stack that we need to update, the first stack that would store the stack, and the second stack that would store "what is the minimum value when this digit is being pushed compared to the previous minimum value"
    # For example with stack = [-1, 0, -3, 4, -7], the minStack would be [-1, -1, -3, -3, -7]
    # And don't forget to pop the minStack too when popping the original stack
    # Time complexity would be O(1)

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minStack == []:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()