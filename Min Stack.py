class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0:
            self.min = [val]
        elif val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        if len(self.stack) != 0:
            top = self.stack.pop()
            if top==self.min[-1]:
                self.min.pop()

    def top(self) -> int:
        top = self.stack.pop()
        self.stack.append(top)
        return top

    def getMin(self) -> int:
        return self.min[-1]
