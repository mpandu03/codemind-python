r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
sum=0
for i in range(r):
    for j in range(c):
        sum+=m[i][j]
print(sum)