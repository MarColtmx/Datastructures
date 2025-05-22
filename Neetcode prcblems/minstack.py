"""Brute Force solution"""

# class MinStack:

#     def __init__(self):
#         self.stack = []
        
#     def push(self, val: int) -> None:
#         self.stack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()
        

#     def top(self) -> int:
#         return self.stack[-1]
        

#     def getMin(self) -> int:
#         tmp = []
#         mini = self.stack[-1]

#         while len(self.stack):
#             mini = min(mini, self.stack[-1])
#             tmp.append(self.stack.pop())
        
#         while len(tmp):
#             self.stack.append(tmp.pop())
#         #print(mini)
#         return mini
    
"""Two stack solution"""

# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.minStack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         val = min(val, self.minStack[-1] if self.minStack else val)
#         self.minStack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()
#         self.minStack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         print(self.minStack[-1])
#         return self.minStack[-1]

"""One stack"""

class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()
        
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min

minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
minStack.push(1)
minStack.getMin() #// return 0
minStack.pop()
minStack.pop()
minStack.top() #    // return 2
minStack.getMin()# // return 1
