class CustomStack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stack = []
    
    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return -1
    
    def increment(self, k, val):
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val

# Example usage:
customStack = CustomStack(3)
customStack.push(1)
customStack.push(2)
print(customStack.pop())  # Output: 2
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.increment(5, 100)
print(customStack.stack)  # Output: [101, 102, 103]
customStack.increment(2, 100)
print(customStack.stack)  # Output: [201, 202, 103]
print(customStack.pop())  # Output: 103
