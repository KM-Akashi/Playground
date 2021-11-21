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

    def isValid(self, s: str) -> bool:
        for si in s:
            if si in ['(', '{', '[']:
                self.push(si)
            elif si in [')', '}', ']']:
                if (si == ')' and self.pop() != '(') or \
                    (si == '}' and self.pop() != '{') or \
                        (si == ']' and self.pop() != '['):
                    return False
        if self.top == -1:
            return True
        else:
            return False
