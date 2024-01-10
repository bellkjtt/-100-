import sys
n=int(sys.stdin.readline().rstrip())
cnt=0
s=0
while s<n:
    cnt+=1
    s+=cnt
print(cnt)