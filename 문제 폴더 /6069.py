import sys
a=[sys.stdin.readline().rstrip()]
k= ['best!!!' if i=='A' else 'good!!' if i=='B' else 'run!' if i=='C' else 'slowly~' if i=='D' else 'what?' for i in a]
for m in k:
    print(m)