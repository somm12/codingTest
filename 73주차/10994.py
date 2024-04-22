n = int(input())
cnt = (n-1)*4 + 1
row = []

for idx in range((cnt//2)+1):
    tmp = []
    for i in range(idx+1):
        if i < idx:
            tmp.append(1)
        else:
            tmp.append(cnt - (idx*2))
    tmp += tmp[:idx]# 대칭 적으로 이어짐.
    row.append(tmp)

tmp = row[:-1]
row += tmp[::-1]# 대칭적으로 거꾸로 이어짐.
for i in range(len(row)):
    s = ''
    for j in range(len(row[i])):
        if j % 2 == 0:
            s+= row[i][j]* '*'
        else:
            s += row[i][j] * ' '
    print(s)

# n 이 3일 때
# 첫 줄의 개수: 1+ (n-1)*4. => n이 1,2,3일 때 각 첫줄의 별 개수는 4개씩 차이가 남.
# 중간 줄 까지 아래와 같은 형태이고, 짝수번째는 *을 그리고 홀수 번째는 빈칸을 나타낸다.
# 9개
# 1 7 1
# 1 1 5 1 1
# 1 1 1 3 1 1 1
# 1 1 1 1 1 1 1 1
# 거꾸로, 같음.
    