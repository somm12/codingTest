def solution(land):
    answer = 0
    for i in range(1,len(land)):
        for j in range(4):
            maxV = -1
            for k in range(4):
                if j != k:
                    maxV = max(maxV,land[i][j] + land[i-1][k])
            land[i][j] = maxV
    return max(land[len(land)-1])

# 땅따먹기