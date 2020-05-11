class MinStack:

    def __init__(self):
        self.numbers=[]
        self.min=None     

    def push(self, x: int) -> None:
        if len(self.numbers) == 0:
            self.min = x
            self.numbers.append([x,x])
        else:
            lastmin=self.min
            self.numbers.append([x,lastmin])
            self.min=min(x,lastmin)
            

    def pop(self) -> None:
        self.min=self.numbers[-1][1]
        self.numbers.pop()

    def top(self) -> int:
        return self.numbers[-1][0]
        

    def getMin(self) -> int:
        return self.min

t=MinStack()
t.push(-1)

print(t.top())
print(t.getMin())



