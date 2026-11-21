t = 10


for _ in range(t):
    c = int(input())
    buildings = list(map(int, input().split()))
    ans = 0
    for i in range(2, c - 2):
        if buildings[i -2] < buildings[i] and  buildings[i -1] < buildings[i] and buildings[i + 2] < buildings[i] and  buildings[i + 1] < buildings[i]:
            cur = min(buildings[i] - max(buildings[i - 2], buildings[i - 1]),
                      buildings[i] - max(buildings[i + 2], buildings[i + 1]))
            # print(cur)
            ans += cur

    print(f"#{_+1} {ans}")


