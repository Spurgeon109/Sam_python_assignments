# qazwsx@123
# password
# acc id : 106198233236
#7358267256
# import smtplib
# import random


# def otpgen():
#     s = ""
#     for i in range(0, 7):
#         s+= str(random.randint(0, 9))
#     s = int(s)
#     return s


# def send(rec, f_path, msg):
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.starttls()
#     pas = open(f_path).read()
#     s.login('yacobtalla@gmail.com', pas)
#     s.sendmail('yacobtalla@gmail.com', rec, msg)
#     s.quit()
class Node:
    def __init__(self, a):
        self.val = a
        self.next = None


def reverse(head):
    prev = None
    temp = head
    while temp != None:
        n = temp.next
        temp.next = prev
        prev = temp
        temp = n
    while prev != None:
        print(prev.val)
        prev = prev.next

li = [2, 3, 4, 5]

head = Node(1)
temp = head
for i in li: 
    temp.next = Node(i)
    temp = temp.next
reverse(head)