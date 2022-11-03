n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s+=i
s=s/len(l)
print("{:.2f}".format(s))