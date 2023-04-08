import heapq

def solution(book_time):
    answer = 0
    book = []
    for i in book_time:
        s,e = i
        s = s.split(":")
        e = e.split(":")
        s = int(s[1]) + int(s[0])*60
        e = int(e[1]) + int(e[0])*60
        book.append((e,s))
    book.sort(key = lambda x: x[1])
    q = []
    heapq.heappush(q,book[0])
    answer = 1
    for i in range(1,len(book)):
        end,start = q[0]
        if end + 10 <= book[i][1]:
            heapq.heappop(q)
            heapq.heappush(q,book[i])
        else:
            answer += 1
            heapq.heappush(q,book[i])
        
    return len(q)
# 호텔대실