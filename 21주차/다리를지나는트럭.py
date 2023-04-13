from collections import deque
def solution(length, weight, truck):
    answer = 0
    bridge = deque([0]*length)
    truck = deque(truck)
    total = 0
    while len(bridge):
        a = bridge.popleft()
        answer += 1
        if a >0:
            total -= a
        if truck:
            if truck[0] + total <= weight:
                x = truck.popleft()
                bridge.append(x)
                total += x
            else:
                bridge.append(0)
         
    return answer