n = int(input())
a = ''
for i in range(2*n-1):
    if i % 2 ==0:
        a += '*'
    else:
        a += ' '

for i in range(n):
    if i % 2 == 0:
        print(a)
    else:
        print(' '+a)