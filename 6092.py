n = int(input())
b = map(int,input().split())
li = [0] * 23

for i in b:
    li[i-1]+=1
print(' '.join(map(str,li)))