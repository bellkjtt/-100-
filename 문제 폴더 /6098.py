import sys

a=[]
for i in range(10):
    a.append(list(map(int,sys.stdin.readline().split())))

d=0
k=1


for i in range(1,len(a)-1):
    if a[i][k]!=0 and d==0 and a[i+1][k]==1:
        a[i][k]=9
        break
    elif a[i][k]!=0 and d==1 and a[i][k+1]==1:
        a[i][k]=9
        break
    
    for j in range(k,9):
        
        if a[i][j+1]==0 and d==0:
            a[i][j]=9
        elif a[i][j+1]==1 and d==0:
            a[i][j]=9
            d=1
            k=j
            break

      
        if a[i][j+1]==0 and d==1:
            a[i][j]=9
        elif a[i][j+1]==1 and d==1:
            a[i][j]=9
            d=0
            k=j
            break
        
for k in a:
    print(' '.join(map(str,k)),sep='')