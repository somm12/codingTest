a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print("*",end='')
    print()
#직사각형 별찍기