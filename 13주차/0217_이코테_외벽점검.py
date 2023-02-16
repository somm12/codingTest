from itertools import permutations


def solution(n,weak,dist):
    result = len(dist) + 1
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
        
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count-1]
            for i in range(start,start+length):
                if position < weak[i]:
                    count += 1
                    if len(dist) < count:
                        break
                    position = weak[i] + friends[count-1]
            result = min(result,count)
    if result > len(dist):
        return -1
    return result
print(solution(12,[1,3,4,9,10],[1,2,3,4]))