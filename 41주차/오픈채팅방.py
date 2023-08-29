def solution(record):
    answer = []
    user = {}
    for s in record:
        arr = s.split()
        uid = arr[1]
        if arr[0] == 'Enter':
            user[uid] = arr[2]
        elif arr[0] == 'Change':
            user[uid] = arr[2] # 최종 닉네임 구하기.
            
    for s in record:
        arr = s.split()
        uid = arr[1]
        if arr[0] == 'Enter': 
            answer.append(user[uid]+'님이 들어왔습니다.')
        elif arr[0] == 'Leave':
            answer.append(user[uid]+'님이 나갔습니다.')
    return answer
# 프로그래머스 카카오 문제