while True:
    x,y,z = map(int,input().split())
    if x == 0 and y == 0 and z == 0:
        break
    arr = [x,y,z]
    arr.sort()
    x,y,z = arr
    if z**2 == (x**2)+ (y**2):
        print("right")
    else:
        print("wrong")
# 백준 .피타고라스 정리.