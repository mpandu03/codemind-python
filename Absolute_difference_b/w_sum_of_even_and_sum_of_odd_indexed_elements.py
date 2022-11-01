n=int(input())
l=list(map(int,input().split()))
s=e=0
for i in range(len(l)):
    if i%2==0:
        e+=l[i]
    else:
        s+=l[i]
print(abs(e-s))