def solution(arr):
    prev = arr[0]
    arr.sort()
    for i in range(1, len(arr)):
        now = arr[i]
        for j in range(prev,0,-1):
            if now % j == 0 and prev % j == 0:
                prev = j * (prev//j) * (now//j)
                break
    return prev
# N개의 최소공배수