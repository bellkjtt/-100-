n = int(input())
sum=0
cnt=0
while True:
    cnt+=1
    if n<=sum:
        break
    else:
        sum+=cnt
print(sum)