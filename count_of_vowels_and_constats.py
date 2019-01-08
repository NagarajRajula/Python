n1=input()
n2=input()
c1,c2,sum=0

for i in n1:
    if i=='a' or 'e':
        c1+=1

for i in n2:
    if(isalpha(i)):
        c2+=1

print(c1,c2)        
