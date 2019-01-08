ar=input()
s2=ar.split(" ")
for j in s2:
    str1=''
    temp=[]
    for i in range(len(j)):
        if j[i]=="z":
            temp[i]="a"
        else:
            n=ord(j[i])
            n+=1
            n=chr(n)
            temp.append(n)
    str1=''.join(str(i) for i in temp)
    print(str1,end=" ")
    
