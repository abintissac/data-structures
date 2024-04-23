class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print("linked list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
n1=Node(5)
s=sll()
s.head=n1
n1=Node(5)
n2=Node(10)
n1.next=n2
n3=Node(6)
n2.next=n3
n4=Node(12)
n3.next=n4
s.traversal()