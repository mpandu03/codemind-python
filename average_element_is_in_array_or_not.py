n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=i
s=s//len(l)
if s in l:
    print("True")
else:
    print("False")