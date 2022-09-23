n=int(input())
c=0
d=1
for i in range(len(str(n))):
    a=int(n)%10
    c+=a
    d*=a
    n=n//10
e=d-c
print(e)
    