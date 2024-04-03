import heapq

n = int(input())
rooms = []
lecture = []
for _ in range(n):
    s,t = map(int,input().split())
    heapq.heappush(lecture,(s,t))

answer =0
while lecture:
    if len(rooms) == 0:
        answer += 1
        s,t = heapq.heappop(lecture)
        heapq.heappush(rooms, (t,s))
    else:
        end,start = rooms[0]
        if end <= lecture[0][0]:# 강의실을 이어서 사용할 수 있다면, 이어서 사용.
            heapq.heappop(rooms)
        else:# 강의실을 이어서 사용할 수 없다면.
            answer += 1
        s,e = heapq.heappop(lecture)
        heapq.heappush(rooms,(e,s))# 수업이 빨리 끝나는 기준으로 heap에 push

print(answer)