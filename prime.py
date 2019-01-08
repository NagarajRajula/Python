n=input()
n=int(n)
f=1
m=n/2
for i in range(2,n):
    if(n%i==0):
        print("not prime")
        f=0
        break;
if f==1 :
    print("prime")
