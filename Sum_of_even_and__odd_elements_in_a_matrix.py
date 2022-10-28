r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
sume=sumo=0
for i in range(r):
    for j in range(c):
        if m[i][j]%2==0:
            sume+=m[i][j]
        else:
            sumo+=m[i][j]
print(sume,sumo)