import numpy as np

n=int(input())
h=np.array(list(map(int,input().split())))

cnt=0
while (1):
    target=h.max()
    if target == 0 :
        print(cnt)
        break
    
    flag = 0
    for i, hi in enumerate(h) :
        if hi == target:
            if flag == 0:
                flag = 1
                cnt+= 1
            h[i]-=1
        else :
            flag=0
