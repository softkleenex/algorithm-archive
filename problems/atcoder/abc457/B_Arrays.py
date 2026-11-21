n = int(input())

ans = []

for _ in range(n):
    temp = list(map(int, input().split()))
    L = temp[0]
    A = temp[1:]
    ans.append(A)

# print(ans)

x, y = map(int, input().split())
print(ans[x -1][y - 1])
