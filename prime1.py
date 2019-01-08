n1=input()
n2=int(n1)
n=int(n2/2)
c=0
print(n)
for i in range(2,n,1):
    if ((n%i)==0):
        c=1
if c==1:
    print(n1," is not a prime")
else:
    print(n1," is a prime")
        
