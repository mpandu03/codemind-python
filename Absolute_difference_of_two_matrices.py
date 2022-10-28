n=int(input())
m=[]
m1=[]
s1=[]
for i in range(n):
    l=list(map(int,input().split()))
    m.append(l)
for j in range(n):
    s=list(map(int,input().split()))
    m1.append(s)
for i in range(n):
    c=[]
    for j in range(n):
        c.append(abs(m[i][j]-m1[i][j]))
    s1.append(c)
for i in s1:
    print(*i)