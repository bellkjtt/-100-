import sys
h,w= map(int,sys.stdin.readline().split())
n=int(sys.stdin.readline())

li = [[0]*w for _ in range(h)]

for i in range(n):
    l,d,x,y =map(int,sys.stdin.readline().split())
    if d==0:
        for j in range(y-1,y-1+l):
            li[x-1][j]=1
    else:
        for j in range(x-1,x-1+l):
            li[j][y-1]=1

for i in li:
    print(' '.join(map(str,i)))

#x부터 x+l 까지로 계산