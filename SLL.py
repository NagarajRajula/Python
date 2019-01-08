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
class SLL:
    
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

    def insert_at_end(self,data):
        newnode=Node()
        newnode.data=data
        cur=self.head
        while cur.get_next()!=None:
            cur=cur.get_next()
            
        cur.set_next(newnode)
        self.length+=1
    
    def insert_at_mid(self,data):
        newnode=Node()
        print("enter position to insert")
        pos=int(input())
        newnode.data=data
        aftr=Node()
        if self.length==0:
            self.head=newnode
        else:
             cur=self.head
             while pos-1:
                 cur=cur.get_next()
                 pos-=1
             '''newnode.get_next(cur.get_next())    
             cur.set_next(newnode)'''

             aftr=cur.get_next()
             newnode.set_next(aftr)
             cur.set_next(newnode)
             
    def count(self):
        cur=self.head
        count1=0
        while cur!=None:
            cur=cur.get_next()
            count1+=1
        print(count1)

    def del_at_begin(self):
        if self.length==0:
            print("Nothing to delete")
        else:
            self.head=self.head.get_next()
            self.length-=1

    def del_at_last(self):
        if self.length==0:
            print("Nothing to delete")
        else:
            prev=self.head
            cur=self.head
            while cur.get_next()!=None:
                prev=cur
                cur=cur.get_next()
            prev.set_next(None)
            self.length-=1
            
    def del_at_pos(self,l):
        print("Enter position to delete:")
        pos=int(input())

        if pos==1:
            '''del_at_begin()
        elif pos==self.length():
             del_at_last()'''
        else:
            k=l-pos
            prev=Node()
            cur=Node()
            cur=self.head
            while k-1:
                prev=cur
                cur=cur.get_next()
                k-=1
            prev.set_next(cur.get_next())
                
    def reverse_list(self):
        prev=Node()
        nex=Node()
        cur=Node()
        cur=self.head
        prev=None
        
        while(cur!=None):
            nex=cur.get_next()
            cur.set_next(prev)
            prev=cur
            cur=nex
        self.head=prev       
                
    def add_1(self,data):
        c=0
        
        cur=self.head
        cur.get_data()
        while(cur!=None):
            d=int(cur.get_data())
        
            sum=c+d+int(a)
            if(sum>=10):
                c=sum%10
                n=int(sum/10)
                sum=n-1    
            cur.set_data(sum)
            cur=cur.get_next()

    def add_lists(self,l1,l2):
        c=0
        prev=None
        temp=None
        
        while(l1!=None or l2!=None):
            fd=0 if l1 is None else l1.get_data()
            sd=0 if l2 is None else l2.get_data()

            sum=c+fd+sd

            c=1 if sum>=10 else 0

            sum=sum if sum<10 else sum%10
            
            temp=Node()
            temp.set_data(sum)

            if self.head is None:
                self.head=temp
            else:
                prev.set_next(temp)

            prev=temp

            if  l1 is not None:
                l1=l1.get_next()
            if l2 is not None:
                l2=l2.get_next()

        if c>0:
            temp.set_next=Node(c)
                
                
    def find_loop(self):
        fp=sp=self.head
        while(sp and fp and fp.get_next()):
            sp=sp.get_next()
            fp=fp.get_next().get_next()

            if sp==fp:
                print("loop found",sp.data)
                self.remove_loop(sp)
                return 1
        return 0
    def remove_loop(self,ln):
        p1=ln
        p2=ln
        k=1
        while(p1.next!=p2):
            p1=p1.next
            k+=1
        print("count=",k)    
        p1=self.head
        for i in range(k):
            d=p2.data
            p2=p2.next
            print(int(d))

        while(p2!=p1):
            
            p2=p2.next
            p1=p1.next
            print(" in while")
        d2=p2.data
        d1=p1.data
        print("p1",int(d1))
        print('p2',int(d2))    
        p2=p2.next
        while(p2.next!=p1):
            p2=p2.next
            print("in 2nd while")
        p2.set_next(None)    


    def merge_lists(self,l2):
        l2n=l2.head
        
        cur=self.head
              
        while(cur!=None and l2n!=None):
            cn=cur.next
            l2n_next=l2n.next

            l2n.next=cn
            cur.next=l2n

            cur=cn
            l2n=l2n_next

        l2.head=l2n    
        

            
mylist=SLL()
'''print("inserting:")
i=int(input())'''


''''mylist.insert_at_begin(9)
mylist.insert_at_begin(9)

mylist.insert_at_begin(9)
mylist.insert_at_begin(1)
'''
l1=SLL()
l2=SLL()
l2.insert_at_begin(8)
l2.insert_at_begin(7)
l2.insert_at_begin(6)
l2.insert_at_begin(5)

l1.insert_at_begin(6)
l1.insert_at_begin(5)
l1.insert_at_begin(4)
l1.insert_at_begin(3)
l1.insert_at_begin(2)
l1.insert_at_begin(1)

l1.print_nodes()

l=l1.list_length()
l1.del_at_pos(l)
l1.print_nodes()

'''l2.merge_lists(l1)

l2.print_nodes()'''

'''l2.head.next.next.next.next.next.next.next.next=l2.head.next.next.next'''

'''
l2.find_loop()
l2.print_nodes()'''

'''mylist.reverse_list()
l2.reverse_list()

mylist.print_nodes()
l2.print_nodes()'''

'''res=SLL()
res.add_lists(mylist.head,l2.head)
res.print_nodes()'''
'mylist.insert_at_begin(11)'
'''
mylist.insert_at_end(6)
mylist.insert_at_end(5)
mylist.insert_at_end(4)
'''
'''mylist.insert_at_mid(3)
'''

'''print("enter element to add")
a=input()

mylist.count()

mylist.print_nodes()

mylist.reverse_list()

mylist.print_nodes()
'''
'''mylist.add_1(a)
mylist.print_nodes()
'''

'''mylist.del_at_begin()

mylist.print_nodes()

mylist.del_at_last()
mylist.print_nodes()
'''
'''mylist.del_at_pos()
mylist.print_nodes()

'''
