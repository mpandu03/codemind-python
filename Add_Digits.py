n=int(input())
c=0
while 1:
    while n>0:
        a=n%10
        c+=a
        n=n//10
    if c<10:
        print(c)
        break
    else:
        n=c
        c=0
