from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

train = [deque([0]* 20) for _ in range(n)]


for _ in range(m):
    command = list(map(int,input().split()))
    if command[0] == 1:
        _,i,x = command
        train[i-1][x-1]=1
    elif command[0] == 2:
        _,i,x = command
        train[i-1][x-1] = 0
    elif command[0] == 3:# 뒤로 한칸씩
        _,i = command
        train[i-1].rotate(1)
        if train[i-1][0] == 1:
            train[i-1][0] = 0
    else:# 앞으로 한칸씩.
        _,i = command
        train[i-1].rotate(-1)
        if train[i-1][-1]:
            train[i-1][-1] = 0


s = set()
for i in range(n):# 같은 패턴은 개수로 세지 않는다.
    tmp = ''
    for v in train[i]:
        tmp += str(v)
    
  
    s.add(tmp)
print(len(s))
# 백준 기차가 어둠을 헤치고 은하수를