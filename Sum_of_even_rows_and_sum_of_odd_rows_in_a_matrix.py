r,c=map(int,input().split())
m=[]
sume=sumo=0
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(r):
    for j in range(c):
        if (i%2==0):
            sume+=m[i][j]
        else:
            sumo+=m[i][j]
print(sume,sumo)
