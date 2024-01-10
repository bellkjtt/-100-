r, g, b = map(int, input().split())
count = 0
for x in range(0, r) :
    for y in range(0, g) :
        for z in range (0, b) :
            print(x,y,z)
            count += 1
print(count)
