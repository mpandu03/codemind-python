a,b=map(int,input().split())
if a<b:
    g=b
else:
    b=a
while True:
    if (g%a==0)and(g%b==0):
        print(g)
        break
    g+=1