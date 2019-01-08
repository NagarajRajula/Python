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
    
class stack_implementation(object):
    def __init__(self):
        self.head=None9
        self.stk=[]
        '''if data:
            for data in data:
                self.push(data)'''
                
    def is_Empty(self):
        return len(self.stk)<=0
    
    def push(self,data):
        temp=Node()
        temp.set_data(data)
        temp.set_next(self.head)
        self.head=temp
        
    def pop(self):
        if self.head is None:
            raise IndexError
        temp=self.head.get_data()
        self.head=self.head.get_next()
        return temp
            
    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.get_data()

'''def check_bal(input1):
    sym=stack_implementation(0)
    bal=0
    for i in input1:
        if i in["(","{","["]:
            sym.push(i)

        else:
            if i.is_Empty():
                bal=0
            else:
                ts=sym.pop()

        if not matches(ts,sym):
            bal=0
        else:
            bal=1

    return bal        '''
        
        

def parChecker(symbolString):
    s = []
    balanced = True
    index = 0
    print(len(symbolString))
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.append(symbol)
        elif symbol==")":
            if len(s)==0:
                balanced = False
                
            else:
                s.pop()

        index = index + 1

    if balanced and len(s)==0:
        return True
    else:
        return False

print(parChecker("(()))"))
print(parChecker('(())'))

    

li=["first","second","third"]
'''
s=stack_implementation(li)

print(s.pop())
print(s.pop())d

print(s.peek())
print(check_bal("([)"))
print(check_bal("{{[][]}()}"))'''

        
