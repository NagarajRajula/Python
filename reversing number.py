#code
t=input()
t=int(t)

while (t!=0):
    t-=1
    i=int(input())
    r=0
    j=0
    while i>0:
       c=i%10
       r=(r*10)+c
       i=i//10
    print(int(r))
    

