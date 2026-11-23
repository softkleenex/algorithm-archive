

def dist_square(x1, y1, x2, y2):
    #print(x1, y1, x2, y2)
    return(
            (x1 - x2) ** 2 + (y1 - y2) ** 2
        )




T = int(input())

for _ in range(0, T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    #print(x1, y1, r1, x2, y2, r2)
    #x1, y1에서 반지름이 r1인 원과 x2, y2에서 반지름이 r2인 원의 접접 개수를 생각해본다면
    #0 > 만나지 않는다, (존재할 수 없다.) 1 > 접한다, 2 > 두 점에서 만난다, -1(무한대) > 두 원이 동일하다.

    #print(dist_square(x1, y1, x2, y2), (r1 + r2)**2)
    if (x1 == x2 and y1 == y2 and r1 == r2):
        print(-1)
    elif(dist_square(x1, y1, x2, y2) == (r1 + r2)**2 or dist_square(x1, y1, x2, y2) == (r1 - r2)**2):#내접의 경우도
        print(1)
    elif((r1 - r2)** 2 < dist_square(x1, y1, x2, y2) < (r1 + r2)** 2):
        print(2)
    else:
        print(0)
