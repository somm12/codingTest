n,k = map(int,input().split())
arr = list(map(int,input().split()))

odd = 0#홀수 개수.
even = 0#짝수 개수
end =0 # 끝 포인터.
answer = 0
for start in range(n):
    while odd <= k and end < n:# 홀수개수가 k개 넘을 때 까지 반복.
        if arr[end]%2 == 1:# 홀, 짝수 개수 세기
            odd += 1
        else:
            even += 1
        end += 1
        if start == 0 and end == n:# 홀수 개수가 K개 이하로 있다면, 답은 전체 배열에서 짝수 개수 와 같다.
            answer = even
            break
    if odd == k+1:# 홀수개수 k개를 넘으면, 짝수 개수 업데이트.
        answer = max(answer,even)
    if arr[start]%2:
        odd -= 1
    else:
        even -= 1
print(answer)
# 가장 긴 짝수 연속한 부분수열