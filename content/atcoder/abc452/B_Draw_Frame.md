---
title: "[AtCoder] B_Draw_Frame"
tags: ["AtCoder", "abc452"]
---

# B_Draw_Frame

이 문제는 AtCoder에서 푼 문제입니다.
이 문제는 **abc452** 콘테스트 문제입니다.

🔗 [문제 바로가기](https://atcoder.jp/contests/abc452/tasks/abc452_b)


---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->

Iterate through H rows to print the grid.
- First/Last row: Print "#" W times.
- Other rows: Print "#" at the start/end, and "." for the middle W-2 cells.

## 💻 코드

```python
h, w = map(int, input().split())

for i in range(h):
    if i == 0 or i == h - 1:
        print("#" * w)
    else:
        print("#" + "." * (w - 2) + "#")

```
