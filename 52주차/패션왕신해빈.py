T = int(input())
for _ in range(T):
    n = int(input())
    dict = {}
    for _ in range(n):
        name,kind = input().split(" ")
        if kind in dict:
            dict[kind] +=1
        else:
            dict[kind] = 1
    total = 1
    
    for v in dict.values():
        total *= (v+1)
    print(total-1)
# 선택을 안하거나 or 선택하거나,
# 같은 종류의 옷은 한가지만 가능. => (x+1) * ( y+1)...... -1 (아무것도 안입는 경우 하나 빼기)
# 백준 문제 2375.