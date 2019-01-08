n=input("enter an no.of elements:")

s=[]
for i in range(int(n)):
    t=input()
    s.append(int(t))
for i in range(int(n)):
    for j in range(i+1,int(n),1):
        for k in range(j+1,int(n), 1):
            if(s[i]!=s[k] and s[j]!=s[k] and s[i]!=s[j] ):
               sum=s[i]+s[j]+s[k]
               if sum==0:
                   print("Yes",s[i],s[j], s[k])
            
    
                
