import sys
a,b=map(bool,(map(int,sys.stdin.readline().rstrip().split())))
print('True' if a!=b else 'False')
# bool은 str을 넣으면 안된다