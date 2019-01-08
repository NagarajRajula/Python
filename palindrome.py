n=input()
n=int(n)
temp=n
s=0
r=0
while n>0:
    r=n%10
    s=r+s*10
    n=n//10
if(temp==s) :
    print("Yes its a palindrome: ",s)    
