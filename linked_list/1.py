class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
# node1=Node(6)
# print(node1.data)
# print(node1.next)
class Sll:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print("singly linked list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
n1=Node(5)
s=Sll()
s.head=n1
n2=Node(6)
n1.next=n2
n3=Node(8)
n2.next=n3
n4=Node(9)
n3.next=n4
s.traversal()