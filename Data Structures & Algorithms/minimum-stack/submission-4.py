class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values = []
        self.cur_min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.cur_min is None or val <= self.cur_min:
            self.cur_min = val
            self.min_values.append(val)
        

    def pop(self) -> None:
        popped_val = self.stack.pop()
        if popped_val == self.cur_min:
            self.min_values.pop()
            self.cur_min = self.min_values[-1] if (len(self.min_values) > 0) else None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_values[-1]
        
