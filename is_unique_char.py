n1=input()
n=list(n1)

c=False
for i in range(len(n1)):
    for j in range(i+1,len(n1)):
        if (n[i]==n[j]):
            c=True
            break
        

if c==True:
      print("is not unique")
else:
    print("is unique")
