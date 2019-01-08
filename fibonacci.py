n=input()
n=int(n)
n0=0
n1=1
sum=0
c=0
#print(n0)
#print(n1)
while c<n :
    print(n0,sep=',')
    sum=n1+n0
    n0=n1
    n1=sum
    c+=1
    
