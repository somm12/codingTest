def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr1[0])
    answer = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            answer[i][j] = arr1[i][j] + arr2[i][j]
            
            
    return answer
# 행렬의 덧셈