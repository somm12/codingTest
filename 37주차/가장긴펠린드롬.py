def solution(s):
    answer = 0

    def isTrue(left,right):
        length = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:# 값이 같으면 길이 +2, 양 방향으로 퍼져서 검사함.
                length += 2
                left -= 1
                right += 1
            else:
                break
        return length
    
    for i in range(len(s)):# 길이가 짝수라면 i,i+1. 홀수라면 i, i+2(중간 기준점을 두고 생기므로 기준점길이도 포함해서 +1)
        answer = max(answer, isTrue(i,i+1), isTrue(i,i+2)+1)

    return answer

# 프로그래머스 lv3 문제
# 투 포인터 이용.
# n: 2500
# O(n^2)