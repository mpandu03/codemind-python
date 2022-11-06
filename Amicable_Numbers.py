n=int(input())
n1=int(input())
s=d=0
for i in range(1,n):
    if n%i==0:
        s+=i
for j in range(1,n1):
    if n1%j==0:
        d+=j
if s==n1 and d==n:
    print("Amicable")
else:
    print("Not Amicable")