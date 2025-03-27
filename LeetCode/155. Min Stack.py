class MinStack:

    # use two stack (list) to maintain the smallest tracking 
    # one stack is to store all input
    # the other stack is to store smallest elements 
    # input will be append to tail of normal stack, 
    #   if this input is smaller than current smallest, append it to 2nd stack  
    #   if input is not smaller, append the 2nd tail to 2nd list again 
    #       this approach keep two lists same length and always have the smallest ele at the tail, so faster to track smallest
    #       tradeoff is the doubled storage space

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack == [] or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
    

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()