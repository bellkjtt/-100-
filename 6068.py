import sys
a=[int(sys.stdin.readline().rstrip())]
k= ['A' if i>=90 else 'B' if i>=70 else 'C' if i>=40 else 'D'  for i in a]
for m in k:
    print(m)