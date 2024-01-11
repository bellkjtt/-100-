import sys
_, *b= map(int,sys.stdin.buffer.read().split())

ba = [[0]*19  for _ in range(19)]

for i in range(0,len(b),2):
    ba[b[i]-1][b[i+1]-1]=1

for i in range(19):
    print(' '.join(map(str,ba[i])))

#buffer를 이용해 시간복잡도를 줄이는 풀이