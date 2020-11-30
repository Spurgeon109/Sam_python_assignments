class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
    
    def insert(self):
        value = int(input("Enter the value to insert: "))
        temp = self
        while temp.next != None:
            temp = temp.next
        temp1 = Node(value)
        temp1.prev = temp
        temp.next = temp1
    def Print_with_next(self):
        temp = self
        while temp != None:
            print(temp.val)
            temp = temp.next
    def Print_with_prev(self):
        temp = self
        while temp.next != None:
            temp = temp.next
        while temp != None:
            print(temp.val)
            temp = temp.prev




if __name__ == "__main__":
    root = Node(int(input("Enter the root value: ")))
    for i in range(0, 3):
        root.insert()
    root.Print_with_prev()
    
    


