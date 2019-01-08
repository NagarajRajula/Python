from itertools import permutations
s1=input()
s2=input()
c=True
s=permutations(s1)
for i in s:
    print(i)
for j in s:
    if(s2!=j):
        c=False
    elif(s2==j):
        c=True
        break
    
        
    
if c==True:
    print("Yes")
else:
    print("No")
    
    
