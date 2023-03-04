def solution(board, moves):
    answer = 0
    columns = [[] for _ in range(len(board)+1)]
    basket = []
    for i in range(len(board)-1,-1,-1):
        for j in range(len(board)-1,-1,-1):
            if board[j][i] != 0:
                columns[i+1].append(board[j][i])
    
    for i in moves:
        if len(columns[i]) > 0:
            p = columns[i].pop()
            if len(basket) > 0:
                if basket[-1] == p:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(p)
            else:
                basket.append(p)
                
    return answer
# 크레인 인형뽑기 게임