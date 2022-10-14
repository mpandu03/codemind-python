a=int(input())
c=0
for j in range (a,a-100,-1):
    n=j
    is_prime=True
    for i in range (2,int(j**0.5)+1):
        if  j%i==0:
            is_prime=False
            break
    if is_prime==True and n!=1:
        c+=1
    if c==1:
        p1=n
        break
c1=0
for k in range (a,a+100,1):
    n1=k
    is_prime1=True
    for e in range (2,int(n1**0.5)+1):
        if  k%e==0:
            is_prime1=False
            break
    if is_prime1==True and n1!=1:
        c1+=1
    if c1==1:
        p2=n1
        break
p3=abs(a-p1)
p4=abs(a-p2)
print(min(p3,p4))