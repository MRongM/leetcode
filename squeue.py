class SQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, x):
        self.stack1.append(x)

    def deleteHead(self):
        n = len(self.stack1)
        if n == 0:
            return -1

        for i in range(n - 1):
            self.stack2.append(self.stack1.pop())
        ans = self.stack1.pop()

        m = len(self.stack2)
        for j in range(m):
            self.stack1.append(self.stack2.pop())
        return ans


q = SQueue()
for i in range(10):
    q.appendTail(i)
print(q.stack1, q.stack2)
q.deleteHead()
q.deleteHead()
print(q.stack1, q.stack2)
