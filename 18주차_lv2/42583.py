from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    sum_weight = 0
    truck_weights = deque(truck_weights)
    trucks_on_bridge = deque([0] * bridge_length)
    while len(trucks_on_bridge):
        answer += 1
        a = trucks_on_bridge.popleft()
        if a > 0:
            sum_weight -= a
        if truck_weights:
            if sum_weight + truck_weights[0] <= weight:
                tmp = truck_weights.popleft()
                trucks_on_bridge.append(tmp)
                sum_weight += tmp
            else:
                trucks_on_bridge.append(0)
    return answer
         
# 다리를 지나는 트럭