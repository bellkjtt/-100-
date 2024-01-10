n = int(input())
print(' '.join(map(str,list(i for i in range(1,n+1) if not i%3==0))))