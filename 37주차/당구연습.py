def cal(x,y, startX, startY, ballX, ballY):
    result = []

    if not (startX == ballX and ballY > startY): # 상
        dist = (startX-ballX)**2 + (2*y - startY- ballY)**2
        result.append(dist)
    if not (startX == ballX and ballY < startY): # 하
        dist = (startX-ballX)**2 + (startY + ballY)**2
        result.append(dist)
    if not (startX > ballX and ballY == startY): # 좌
        dist = (startX+ballX)**2 + (startY - ballY)**2
        result.append(dist)
    if not (startX < ballX and ballY == startY): # 우
        dist = (2*x - startX-ballX)**2 + (startY - ballY)**2
        result.append(dist)
    return min(result)

def solution(m, n, startX, startY, balls):
    answer = []
    for ballX,ballY in balls:
        answer.append(cal(m,n, startX, startY, ballX, ballY))
    return answer
# 당구연습 프로그래머스 문제.
# 대칭 이용
