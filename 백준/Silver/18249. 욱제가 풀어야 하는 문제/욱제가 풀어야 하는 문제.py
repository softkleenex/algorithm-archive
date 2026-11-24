import sys
import math
import itertools
input = sys.stdin.readline



ans = [0, 1, 2, 3]
x = pow(10, 9) + 7


for i in range(4, 191229 + 1):
    ans += [ans[i - 2] + ans[i -1]]
    ans[-1] = ans[-1] % x

T = int(input())

for _ in range(T):
    n = int(input())
    print(ans[n])
