# implementing a stack
class Stack:
    def __init__(self, n):
        self.size = n - 1
        self.top = -1
        self.arr = [0] * n
    def push(self, val):
        if self.top < self.size: 
            self.top+= 1
            self.arr[self.top] = val

        else:
            print("Overflow")
            return False;

    def pop(self):
        if self.top == -1: print("underflow")
        else:
            del self.arr[self.top]
            self.top-= 1
    def Print(self):
        print("Printing all the elements")
        for i in self.arr: print(i)


if __name__ == "__main__":
    s = Stack(5)
    s.push(int(input()))
    s.push(int(input()))
    s.push(int(input()))
    s.push(int(input()))
    s.push(int(input()))
    s.push(int(input()))
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.Print()

