n=input("enter an no.of elements:")

s=[]
for i in range(int(n)):
    t=input()
    s.append(int(t))
for i in range(int(n)):
    for j in range(i+1,int(n),1):
        for k in range(j+1,int(n), 1):
            for l in range(k+1, int(n), 1):
                if(s[i]==0 or s[j]==0 or s[k]==0 or s[l]==0):
                   
                    if(s[i]!=s[k] and s[j]!=s[k] and s[i]!=s[j] and s[i]!=s[l] and s[j]!=s[l] and s[k]!=s[l]):
                       sum=s[i]+s[j]+s[k]+s[l]
                       if sum==0:
                           print("Yes",s[i],s[j], s[k],s[l])
                    
    
                
