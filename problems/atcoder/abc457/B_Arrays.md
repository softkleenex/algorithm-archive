---
title: "[AtCoder] B_Arrays"
tags: ["AtCoder", "abc457"]
---

# B_Arrays

이 문제는 AtCoder에서 푼 문제입니다. 
이 문제는 **abc457** 콘테스트 문제입니다. 

🔗 [문제 바로가기](https://atcoder.jp/contests/abc457/tasks/abc457_b)


---

When solving this problem, keep in mind that the x and y coordinates in the problem description are reversed compared to Python's 2D list indexing.


## 💻 코드

```python
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

```
