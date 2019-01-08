n=[]
#!temp=0
targ=input('enter target:')
tr=0
j=0
print(type(targ))
su=int(targ)
c=int(input("enter no.of inputs"))
for k in range(c):
    n.append(int(input()))

for i in range(c):
    j=i+1
    while j<c:
        #!print (i,j)
        temp=0
        if tr==1:
            break
        else:
            temp=n[i]+n[j]
            #!print(temp,targ)
           #!print (n[i],'+',n[j])
            if temp == su:
                print (n[i] ,'+', n[j], '=', temp)
                tr=1
                break
        j+=1
    #!print (temp)
    
if tr==0:
    print("FO")
