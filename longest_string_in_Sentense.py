sen=input()
s=sen.split(" ")
j=s[0]
print(s[0])
for i in s:
    if len(i)>len(j):
        j=i
print(j)        
    
