import sys
a=[int(sys.stdin.readline().rstrip())]
k= list('spring' if i//3==1 else 'summer' if i//3==2 else 'fall' if i//3==3 else 'winter' for i in a)
for i in k:
    print(i)