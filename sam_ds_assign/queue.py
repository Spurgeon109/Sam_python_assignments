class queue:
    def __init__(self, n):
        self.n = n
        self.arr = [0] * n
        self.f = 0
        self.r = 0
    def enqueue(self, val):
        if self.f <= n-1:
            self.arr[self.f] = val
            self.f+= 1
        else:
            print("Full")
    def Print(self):
        for i in range(self.f -1 , self.r-1, -1):
            print(self.arr[i])
    def dequeue(self):
        if self.f == self.r:
             print("Empty")
        else:
            self.r+= 1
            self.n-= 1
            print("dequeued")
        

if __name__ == "__main__":
    n = int(input())
    q = queue(n)
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    q.enqueue(400)
    q.enqueue(500)
    q.enqueue(600)
    q.Print()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()

    
