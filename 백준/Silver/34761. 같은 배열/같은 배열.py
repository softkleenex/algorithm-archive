import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# print(a)
# print(b)

if a == b[0 : n] and set(b[n : ]).issubset(set(a)):
    print("YES")
else:
    print("NO")
