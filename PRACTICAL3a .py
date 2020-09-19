class Stack:
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, e):
        self.data.append(e)

    def top(self):
        if self.is_empty():
            print('Stack is Empty')
        return self.data[-1]
    
    def pop(self):
        if self.is_empty():
            print('Stack is Empty')
        return self.data.pop()

z = Stack()
print(z.is_empty())
z.push(5)
z.push(7)
z.push(9)
z.push(6)
z.push(2)
print(z.top())
print(z.__len__())
z.pop()
