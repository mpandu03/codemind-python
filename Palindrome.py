j=int(input())
rev=0
n=j
while n>0:
    a=n%10
    rev=rev*10+a
    n=n//10
if j==rev:
    print("True")
else:
    print("False")
    