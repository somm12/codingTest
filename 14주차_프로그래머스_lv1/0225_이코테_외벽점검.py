from itertools import permutations
def solution(n,weak,dist):
    length = len(weak)
    res = len(dist) + 1
    for i in range(length):
        weak.append(weak[i]+n)
    print(weak)
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count-1]
            for now in range(start, start+length):
                if position < weak[now]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[now] + friends[count-1]
            res = min(res,count)
    if res > len(dist):
        answer = -1
    return res
print(solution(12,[1,5,6,10],[1,2,3,4]))