n=input("enter no.of")
a=[]
for i in range(int(n)):
    t=input()
    a.append(int(t))
for i in range(int(n)):
    for j in range(i+1,int(n),1):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print (a)            

for i in range(int(n)):
    
    
    
