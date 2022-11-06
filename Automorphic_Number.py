n=int(input())
a=n*n
d=len(str(n))
c=('1'+int(d)*'0')
c=int(c)
b=a%c
if n==b:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")