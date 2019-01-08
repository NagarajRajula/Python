
def palind(i):
    i=i.replace(" ","")
    i=i.lower()

    d=dict()
    print(d)
    for j in i:
        if j in d:
            d[j]+=1
        else:
            d[j]=1
    
    o = 0
    for k,v in d.items():
        if v % 2 !=0 and o == 0:
            o +=1
        elif v % 2 !=0 and o !=0:
            return False
    return True
    
n=input()
print(palind(n))
            
