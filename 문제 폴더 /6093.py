n = int(input())
b = list(map(int,input().split()))

for i in range(len(b),0,-1):
    print(b[i-1])