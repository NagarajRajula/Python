n=input("enter a number : ")
n=int(n)
s=0
#n=1634
ord=len(str(n))
temp=n
while n > 0 :
    r=n%10
    s+=r**ord
    n=n//10
    #print(s)
if s==temp:
    print(s,"is an amstrong number")
else :
    print("not")
