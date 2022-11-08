n=int(input())
j=0
while True:
    s=0
    while n>0:
        r=n%10
        s+=(r*r)
        n=n//10
    if s<10:
        j=s
        break
    else:
        n=s
if j==1 or j==7:
    print("True")
else:
    print("False")