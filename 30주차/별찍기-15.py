n = int(input())
for i in range(n):
    for _ in range(n-1-i):
        print(" ",end='')
    for j in range(2*i + 1):
        if j == 0 or j == 2*i:
            print("*", end='')
        else:
            print(' ',end='')
    print()