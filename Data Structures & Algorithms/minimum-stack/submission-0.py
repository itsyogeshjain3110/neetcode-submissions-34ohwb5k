class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = [] 
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            min_val = val
        else:
            min_val = min(self.min_stack[-1], val)
        self.min_stack.append(min_val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
        
