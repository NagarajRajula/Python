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
    
class merge_2_lists:
    
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
            
            
           
    def merge2(self,l2):
        temp=self.head

        while temp.next!=None:
            temp=temp.next
        temp.next=l2.head




    def partition(self):
        temp=self.head
        k=5
        l3=Node()
        l3=None
        l5=Node()
        l4=Node()
        l4=None
        l5=None
        
        while temp!=None:
            print(temp.data)
            if temp.data < k:
                if l3==None:
                    l3=temp
                    print(l3.data)
                    l3=l3.next
                else:
                    l3.next=temp
                    print(l3.data)
                    l3=l3.next

                    
            elif temp.data > k:
                if l5==None:
                    l5=temp
                else:
                    l5.next=temp
                    l5=l5.next
                
                
            elif k==temp.data:
                if l4==None:
                    l4=temp
                else:
                    l4.next=temp
                    l4=l4.next

            temp=temp.next        
                    
        '''l5.next=None
        
        l3.next=l4
        l4.next=l5'''
        print()
        while l3!=None:
            print(l3.data,"->",end="")
            l3=l3.next
        print()    
        while l4!=None:
            print(l4.data,"->",end="")
            l4=l4.next
        print()
        while l5!=None:
            print(l5.data,"->",end="")
            l5=l5.next
          


        
l1=merge_2_lists()
l2=merge_2_lists()

l1.insert_at_begin(1)
l1.insert_at_begin(2)
l1.insert_at_begin(10)
l1.insert_at_begin(5)

l1.insert_at_begin(8)
l1.insert_at_begin(5)

l1.insert_at_begin(3)

l1.print_nodes()


l1.partition()



'''l1.merge_lists(l2)
l1.print_nodes()
'''
