import math
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

answer = L - (max(math.ceil(B/D) ,math.ceil(A/C)))
print(answer)
# 백준 방학숙제