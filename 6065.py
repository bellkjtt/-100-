import sys
a=list(map(int,sys.stdin.readline().rstrip().split()))
k=[i for i in a if i%2==0]
for i in k:
    print(i)