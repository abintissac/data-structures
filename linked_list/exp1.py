class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("error")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end="")
    def count(self):
        count=0
        temp = self.head
        while temp!=None:
            count+=1
            temp = temp.next
        print(count)
s=sll()
n = Node(10)
s.head =n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next=n2
n3 = Node(40)
n2.next = n3
s.display()
s.count()