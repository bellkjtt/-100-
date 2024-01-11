n = int(input())
b = list(map(int,input().split()))
print(min(b))
#내부함수 min을 쓰는 방법 -> 고전적
#문제 의도가 아님

n = int(input())
b = list(map(int,input().split()))
d=b[0]
for i in range(n):
    if d>=b[i]:
        d=b[i]
print(d)

#비교 연산을 통한 DP
#문제 의도임
