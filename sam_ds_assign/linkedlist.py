class node:
    def __init__(self, a):
        self.val = a
        self.next = None

def create():
    n = int(input("Enter the count"))
    root, temp = None, None
    for _ in range(n):
        if root == None:
            root = node(int(input()))
            temp = root
        else:
            temp.next = node(int(input()))
            temp = temp.next
    if root == None: print("Empty list")
    else: print("List created with size {0}".format(n))
    return root

def printList(root):
    temp = root
    while temp != None:
        print("--> {0}".format(temp.val))
        temp = temp.next

def insertNodeend(root, val):
    temp = root
    while temp.next != None: temp = temp.next
    temp.next = node(val)
    printList(root)
    print("Inserted at the end")

def insertNodebeg(root, val):
    temp1 = node(val)
    temp1.next = root 
    printList(temp1)
    print("Inserted at the begining")  
    return temp1

def Insertatpos(root):
    pos = int(input("Enter the posistion"))
    v = int(input("Enter the value"))
    temp = root
    while pos > 1:
        temp = temp.next
        pos-= 1
    temp1 = node(v)
    temp1.next = temp.next.next
    temp.next = temp1
    printList(root)
    print("Inserted at posistion {0}".format(pos))

def reverseLinkedList(root):
    print("Reversing a linked list")
    p, n, temp = None, None, root
    while temp != None:
       n = temp.next
       temp.next = p
       p = temp
       temp = n
    root = p
    printList(root)





if __name__ == "__main__":
    root = create()
    reverseLinkedList(root)
    
    