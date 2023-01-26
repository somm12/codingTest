def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff == 1:
            if [x,y-1,0] in answer or [x+1, y-1,0] in answer or [x-1,y,1] in answer and [x+1,y,1] in answer:
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y, stuff, operate = frame
        if operate == 0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        if operate == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)

# 대표적인 시뮬레이션 문제로 문제의 조건에 정확하게 코드로 옮기는 것이 중요