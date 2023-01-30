from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
a = list(map(int, input().split()))
op = []
for i in range(4):
    if i == 0:
        for _ in range(a[i]):
            op.append('+')
    elif i == 1:
        for _ in range(a[i]):
            op.append('-')
    elif i == 2:
        for _ in range(a[i]):
            op.append('x')
    else:
        for _ in range(a[i]):
            op.append('//')
maxV = (10**9) * -1
minV = (10**9) 

for ops in list(set(permutations(op,n-1))):
    temp = arr[0]
    for i in range(n-1):
        if ops[i] == '+':
            temp += arr[i+1]
        elif ops[i] == '-':
            temp -= arr[i+1]
        elif ops[i] == 'x':
            temp *= arr[i+1]
        else:
            if temp < 0:
                temp = (abs(temp)//arr[i+1])* -1
            else:
                temp //= arr[i+1]
    maxV = max(maxV, temp)
    minV = min(minV, temp)
print(maxV)
print(minV)