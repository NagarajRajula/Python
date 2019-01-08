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
class Remove_dup:    
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
    
    def print_nodes(self):
        cur=Node()
        cur=self.head
        while cur!=None:
            print(cur.data,"-->",end="")
            cur=cur.get_next()
        print()    
    def remove_dup(self,l):
        temp=Node()
        temp=self.head
        for i in range(l):
            new=Node()
            new=temp.next
            for j in range(i+1,l):
                prev=Node()
                prev=new
                while new.next!=None:
                    new=new.next
                    if new.data==temp.data:
                        print(new.data)
                        prev.next=new.next
                        return new.data
                        
                
            temp=temp.next       

l1=Remove_dup()
l1.insert_at_begin(4)
l1.insert_at_begin(3)
l1.insert_at_begin(2)
l1.insert_at_begin(1)
l1.insert_at_begin(2)
l1.insert_at_begin(5)
l=l1.list_length()

d=l1.remove_dup(l)

l1.print_nodes()
