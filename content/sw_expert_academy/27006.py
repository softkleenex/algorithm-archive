x = int(input())

for _ in range(x):
    c = int(input())
    tile1 = []

    for _2 in range(c):
        tile1.append(list(input()))

    def check_tile2(d):
        for i in range(c):
            for j in range(i + 1, c):
                if tile1[i][(j + d) % c] != tile1[j][(i + d) % c]:
                    return 0
        return 1

    ans = 0

    for d in range(c):
        if check_tile2(d):
            ans += c

    print(ans)
