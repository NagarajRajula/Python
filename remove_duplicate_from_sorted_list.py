n=input("enter no. of elements:")
a=[]
for i in range(int(n)):
    t=input()
    a.append(int(t))
for i in range(int(n)):
    for j in range(i+1,int(n),1):
        if a[i]>=a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
for i in range(int(n)):
    
    if i<int(n)-1:
        j=i+1
        if a[i]==a[j]:
            del a[i]  

print(a)
