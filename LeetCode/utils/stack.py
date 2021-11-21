class Solution:
    stack = []
    top = -1

    def pop(self):
        if self.top == -1:
            return None
        else:
            self.top -= 1
            return self.stack[self.top+1]

    def push(self, value):
        self.top += 1
        if self.top == len(self.stack):
            self.stack.append(value)
        else:
            self.stack[self.top] = value

    def len(self):
        return self.top+1

    def info(self):
        print(self.stack[:self.top+1])
