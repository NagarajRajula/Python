n=input()
l=len(n)-1

res=""
res+=n[0]
c=1
for i in range(l):
    if(n[i]==n[i+1]):
            c+=1
    else:
        if (c >= 1):
            res+=str(c)
        res+=n[i+1]
        c=1

if(c>=1):
    res+=str(c)
        
        
        
print(res)            
