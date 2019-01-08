def one_away(s1,s2):
    
    if (len(s1)==len(s2)):
        c=0
        for i in range(len(s1)):
            if s1[i] != s2[i] :
                c+=1
                if c>=2:
                    return False
                return True

    else:
         d=len(s1)-len(s2)
         if d== -1 or d==1:
             return True
n1=input()
n2=n1.split(",")

k=one_away(n2[0],n2[1])
print(k)
