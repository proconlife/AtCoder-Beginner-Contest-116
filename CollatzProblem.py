s=int(input())

a=s
cnt=1
dic={a:1}
while (1):
    if a % 2 == 1 :
        a=3*a+1
    else:
        a=a/2
    if a in dic :
        print(cnt+1)
        break
    dic[a]=1
    cnt+=1
