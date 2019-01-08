class Node:
    def __init__(self):
        self.data=None
        self.next=None
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


class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

    
class Palindrome_checkin:
    
    def __init__(self,head=None):
        self.head=head
        self.length=0
    def insert_at_begin(self,data):
        newnode=Node()
        newnode.data=data
        if self.length==0:
            self.head=newnode
        else:
            newnode.set_next(self.head)
            self.head=newnode
        
        self.length+=1
        return newnode.data
    
    def list_length(self):
        curr=self.head
        count=0
        while curr!=None:
            count+=1
            curr=curr.get_next()
        return count    
    def palin(self):
        f=1
        s=Stack()
        cur=self.head
        while cur is not None:
            s.push(cur.get_data())
            cur=cur.next

        
        print(s.size())
        cur2=self.head
        while cur2 is not None:
            print(s.pop(),cur2.get_data())
            if(cur2.get_data()!=s.pop()):
                f=0
                
                
            
        if f==0:print("Not a palindrome")
        else:print("Its a palindrome")
        


l2=Palindrome_checkin()
l2.insert_at_begin('R')
l2.insert_at_begin('A')
l2.insert_at_begin('D')
l2.insert_at_begin('A')
l2.insert_at_begin('R')

l2.palin()
