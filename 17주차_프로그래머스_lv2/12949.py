def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for k in range(len(arr2[0])):
            tmp = 0
            for j in range(len(arr1[0])):
                tmp += (arr1[i][j] * arr2[j][k])
            answer[i].append(tmp)
    return answer
# 행렬의 곱셈