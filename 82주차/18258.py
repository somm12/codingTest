import sys
input = sys.stdin.readline # 200만줄 입력..
from collections import deque
q = deque()
n = int(input())
for _ in range(n):
    command = input().rstrip().split(" ")# readline사용시, Input에 줄바꿈 문자 없애는 것 주의.
    
    if len(command) > 1:
        q.append(command[1])
    else:
        if command[0] == "pop":
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())
        elif command[0] == "size":
            print(len(q))
        elif command[0] == "empty":
            if len(q) == 0:
                print(1)
            else:
                print(0)
        elif command[0] == "front":
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])
        elif command[0] == "back":
            if len(q)==0:
                print(-1)
            else:
                print(q[-1])
# 백준 큐2