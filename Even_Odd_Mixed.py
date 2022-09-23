n=int(input())
c=d=0
for i in str(n):
    a=int(n)%10
    n=n//10
    if a%2==0:
        c+=1
    else:
        d+=1
if c!=0 and d==0:
    print('Even')
elif d!=0 and c==0:
    print('Odd')
else:
    print('Mixed')
    