import sys
n=int(sys.stdin.readline())
cnt=0
s=0
while cnt<=n:
    if cnt%2==0:
       s+=cnt
    cnt+=1
print(s)