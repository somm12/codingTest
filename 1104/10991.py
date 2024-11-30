n = int(input())
for i in range(n):
    empty = ' '*(n-1-i) # 공백 부분.
    star = ['*'] * (i+1) # 별 개수 부분.
    star= ' '.join(star) # 별은 한 개의 공백을 가지고 찍힌다.
    print(empty+star)
# 백준 별찍기 - 16