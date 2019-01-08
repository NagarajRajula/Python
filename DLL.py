class Node:
    def __init__(self,data,next,prev):
        self.data=data
        self.next=next
        self.prev=prev
    def set_data(self,data):
        self.data=data
    def get_data(self):
        return self.data
    def set_next(self,next):
        self.next=next
    def get_next(self):
        return self.next
    def has_next(self):
        return self.next!=None
    def set_prev(self,prev):
        self.prev=prev
    def get_prev(self):
        return self.prev
    
class DLL:
    
    def __init__(self,head=None):
        self.head=head
        self.length=0

    def list_length(self):
        curr=self.head
        count=0
        while curr!=None:
            count+=1
            curr=curr.get_next()
        return count    

    def print(self):
        cur=self.head
        while cur!=None:
            print(cur.data,"<-->",end="")
            cur=cur.get_next()
        print()   

    def add_f(self,data):
        newnode=Node(data,None,None)
        if self.head is None:
            self.head=self.tail=newnode
        else:    
            newnode.set_next(self.head)
            self.head.set_prev(newnode)
            self.head=newnode
        self.length+=1

li=DLL()
li.add_f(5)
li.add_f(6)
li.add_f(7)
li.add_f(8)
li.add_f(9)
li.print()
