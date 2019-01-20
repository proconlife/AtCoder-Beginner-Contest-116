a,b,c=map(int,input().split())
if a > c and a > b : print(int(c*b/2))
if b > a and b > c : print(int(a*c/2))
if c > a and c > b : print(int(a*b/2))
