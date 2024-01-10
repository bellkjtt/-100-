import sys
a=[int(sys.stdin.readline().rstrip())]
k= [('C','D') if i>=0 else ('A','B') for i in a]
k2= [k[0][0] if j%2==0 else k[0][1] for j in a]
for m in k2:
    print(m)