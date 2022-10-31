n=int(input())
a=0
b=1
j=0
if n==0 or n==1:
    print("True")
else:
    for i in range(1,n):
        c=a+b
        a=b
        b=c
        if c==n:
            j=1
            break
if j==1:
    print("True")
else:
    print("False")