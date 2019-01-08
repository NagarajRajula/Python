import math

n1=[i for i in input().split(',')]
n2=[]
c,h=50,30

for i in n1:
    n2.append(math.sqrt(2*c*float(i)/h))
    
print(n2)    
