class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.inc = defaultdict(int)
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        idx = len(self.stack) - 1
        top = self.stack.pop() + self.inc[idx]
        self.inc[idx - 1] += self.inc[idx]
        self.inc[idx] = 0
        return top
        

    def increment(self, k: int, val: int) -> None:
        self.inc[min(k - 1, len(self.stack) - 1)] += val
