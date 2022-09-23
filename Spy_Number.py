n=int(input())
c=0
d=1
while n>0:
    a=n%10
    c+=a
    d*=a
    n=n//10
if c==d:
    print("Spy Number")
else:
    print("Not Spy Number")