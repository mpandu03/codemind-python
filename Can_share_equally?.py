a,b=map(int,input().split())
if a%2==1 and b==0:
    print('NO')
elif a==0 and b%2==1:
    print('NO')
elif (a*1+b*2)%2==0:
    print('YES')
else:
    print('NO')