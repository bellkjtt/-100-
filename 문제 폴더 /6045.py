import sys
a,b,c=map(int,sys.stdin.readline().rstrip().split())
k=a+b+c
print('%d %0.2f' % (k,k/3))