import sys
a=[]
for i in range(19):
    a.append(list(map(int,sys.stdin.readline().rstrip().split())))
  
n=int(input())
for i in range(n):
    b,c= sys.stdin.readline().rstrip().split()
    print(b,c)
    for j in range(19):
        if a[j][int(c)-1]==0:

            a[j][int(c)-1]=1
        else:
            a[j][int(c)-1]=0
        
        if a[int(b)-1][j]==0:
            a[int(b)-1][j]=1
        else:
            a[int(b)-1][j]=0
        
for i in a:
    print(' '.join(map(str,i)),sep='\n')

#십자를 뒤집고 뒤집는데 있어서, 어느걸 먼저 뒤집어도 상관 없다.