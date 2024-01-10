import sys
n=int(sys.stdin.readline().rstrip())

for i in range(1,n+1):
    k=str(i)
    if (k[-1]=='3') or (k[-1]=='6') or (k[-1]=='9'):
        print('X',end=' ')
    else:
        print(i,end=' ')