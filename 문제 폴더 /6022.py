import sys
s= str(sys.stdin.readline().rstrip())

for i in range(0,len(s),2):
    print(s[i:i+2],end=" ")