class infix_to_post(object):
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return (self.items==[])
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return sel.items.pop()
    def peek(self):
        return self.items[-1]
    def __str__(self):
        return str(self.items)

def intopost(infi):
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    ops=infix_to_post()
    post=[]
    tokenlist=infi.split()
    for token in tokenlist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWZXY" or "1234567890":
            post.append(token)
        elif token=='(':
            ops.push(token)
        elif token==')':
            toptoken=ops.pop()
            while toptoken!=')':
                post.append(toptoken)
                toptoken=ops.pop()
        else:
            while(not ops.is_empty()) and (prec[ops.peek()]>=prec[token]):
                post.append(ops.pop())
            ops.push(token)

    while not ops.is_empty():
        post.append(ops.pop())
    
    return" ".join(post)
print(intopost("A*B+C*D"))
print(intopost("(a+b)*c-(d-e)*(f+g)"))


        
