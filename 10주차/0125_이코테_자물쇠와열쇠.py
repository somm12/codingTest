from glob import glob


def rotate_90(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = a[i][j]
    return result
# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    # 90, 180, 270, 360 4가지 경우의 회전 + 맞물리는지 확인.
    for _ in range(4):
        key = rotate_90(key)
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False
# 다시풀기**


def rotate(key):
    length = len(key)
    new_key = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            new_key[j][length-1-i] = key[i][j]
    return new_key
def solution(key,lock):
    global result
    result = True
    n = len(lock)
    m = len(key)
    new_lock = [[0]*n*3 for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    for _ in range(4):
        key = rotate(key)
        for x in range(2*n):
            for y in range(2*n):
                result = True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                for i in range(n,n*2):
                    for j in range(n,n*2):
                        if new_lock[i][j] != 1:
                            result = False
                if result:
                    return result
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return result
print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))

