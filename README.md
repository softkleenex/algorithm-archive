<div align="center">

# 🚀 Softkleenex's Coding Training

[![Auto Format](https://github.com/softkleenex/algorithm-archive/actions/workflows/auto_format.yml/badge.svg)](https://github.com/softkleenex/algorithm-archive/actions/workflows/auto_format.yml)
[![Obsidian](https://img.shields.io/badge/Obsidian-483699?style=flat&logo=obsidian&logoColor=white)](https://obsidian.md/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)

**알고리즘 문제 풀이 아카이브 (Obsidian)**

[🌐 블로그 바로가기](https://softkleenex.github.io/posts/)

</div>

---

## 📝 소개 (Introduction)

안녕하세요! 이 저장소는 제가 해결한 알고리즘 문제들의 소스 코드와 저만의 풀이(해설)를 기록하는 공간입니다. 
동시에 작성된 마크다운(`.md`) 파일들은 **GitHub Pages**를 통해 정적 블로그 웹사이트로 자동 배포되어 나만의 포트폴리오로 활용됩니다.

단순한 코드 저장소가 아닌, **완전 자동화된 CI/CD 파이프라인**을 갖춘 현대적인 개발 블로그 시스템입니다.

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white">
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB">
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white">
  <img src="https://img.shields.io/badge/Obsidian-483699?style=for-the-badge&logo=obsidian&logoColor=white">
  <img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white">
</div>

---

## ⚙️ 자동화 파이프라인 (Automated Workflow)

사람 손이 들어가지 않는다. 문제를 풀면 저장소에 쌓이는 것까지가 전부다.

1. **Solve & Auto-Push:** [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub) 익스텐션이 정답 처리된 문제의 소스 코드를 저장소에 자동 커밋한다.
2. **Auto-Formatting:** `scripts/format_problems.py` 가 코드를 마크다운으로 병합하고, `scripts/update_readme.py` 가 위 통계판을 다시 만든다. 둘 다 `auto_format.yml` 이 돌린다.
3. **Archive:** 여기까지다. 웹 배포는 하지 않는다 — 문제 설명이 원 사이트 발췌라 공개 게시 대상이 아니다.

문제별 회고란은 두지 않는다. 풀이 과정은 코드와 그 주석으로 남고, 따로 적어 둘 칸을 만들어도 쓰지 않았다(382문제 중 0건). 글로 쓸 만한 게 생기면 그때 [블로그](https://softkleenex.github.io/posts/)에서 형식을 정해 직접 쓴다.

---

## 📊 성과 대시보드 (Dashboard)

<!-- problems:start -->
### 🏆 Algorithm Solving Status

**Total Solved: 397 Problems** (Baekjoon: 382, AtCoder: 15)

<details>
<summary>💡 <b>전체 풀이 문제 목록 (클릭하여 펼치기)</b></summary>
<br>

| 플랫폼 | 번호 | 문제 이름 | 난이도 | 풀이 링크 |
| :--- | :--- | :--- | :--- | :--- |
| Baekjoon | 1000 | A＋B | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1000.%E2%80%85A%EF%BC%8BB/README.md) |
| Baekjoon | 1001 | A－B | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1001.%E2%80%85A%EF%BC%8DB/README.md) |
| Baekjoon | 1003 | 피보나치 함수 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1003.%E2%80%85%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98%E2%80%85%ED%95%A8%EC%88%98/README.md) |
| Baekjoon | 1008 | A／B | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1008.%E2%80%85A%EF%BC%8FB/README.md) |
| Baekjoon | 1009 | 분산처리 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1009.%E2%80%85%EB%B6%84%EC%82%B0%EC%B2%98%EB%A6%AC/README.md) |
| Baekjoon | 1012 | 유기농 배추 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1012.%E2%80%85%EC%9C%A0%EA%B8%B0%EB%86%8D%E2%80%85%EB%B0%B0%EC%B6%94/README.md) |
| Baekjoon | 1018 | 체스판 다시 칠하기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1018.%E2%80%85%EC%B2%B4%EC%8A%A4%ED%8C%90%E2%80%85%EB%8B%A4%EC%8B%9C%E2%80%85%EC%B9%A0%ED%95%98%EA%B8%B0/README.md) |
| Baekjoon | 1021 | 회전하는 큐 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1021.%E2%80%85%ED%9A%8C%EC%A0%84%ED%95%98%EB%8A%94%E2%80%85%ED%81%90/README.md) |
| Baekjoon | 1032 | 명령 프롬프트 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1032.%E2%80%85%EB%AA%85%EB%A0%B9%E2%80%85%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8/README.md) |
| Baekjoon | 1037 | 약수 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1037.%E2%80%85%EC%95%BD%EC%88%98/README.md) |
| Baekjoon | 1058 | 친구 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1058.%E2%80%85%EC%B9%9C%EA%B5%AC/README.md) |
| Baekjoon | 1075 | 나누기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1075.%E2%80%85%EB%82%98%EB%88%84%EA%B8%B0/README.md) |
| Baekjoon | 1076 | 저항 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1076.%E2%80%85%EC%A0%80%ED%95%AD/README.md) |
| Baekjoon | 1080 | 행렬 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1080.%E2%80%85%ED%96%89%EB%A0%AC/README.md) |
| Baekjoon | 1085 | 직사각형에서 탈출 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1085.%E2%80%85%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95%EC%97%90%EC%84%9C%E2%80%85%ED%83%88%EC%B6%9C/README.md) |
| Baekjoon | 1100 | 하얀 칸 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1100.%E2%80%85%ED%95%98%EC%96%80%E2%80%85%EC%B9%B8/README.md) |
| Baekjoon | 1149 | RGB거리 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1149.%E2%80%85RGB%EA%B1%B0%EB%A6%AC/README.md) |
| Baekjoon | 1157 | 단어 공부 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1157.%E2%80%85%EB%8B%A8%EC%96%B4%E2%80%85%EA%B3%B5%EB%B6%80/README.md) |
| Baekjoon | 1158 | 요세푸스 문제 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1158.%E2%80%85%EC%9A%94%EC%84%B8%ED%91%B8%EC%8A%A4%E2%80%85%EB%AC%B8%EC%A0%9C/README.md) |
| Baekjoon | 1181 | 단어 정렬 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1181.%E2%80%85%EB%8B%A8%EC%96%B4%E2%80%85%EC%A0%95%EB%A0%AC/README.md) |
| Baekjoon | 1182 | 부분수열의 합 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1182.%E2%80%85%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4%EC%9D%98%E2%80%85%ED%95%A9/README.md) |
| Baekjoon | 1197 | 최소 스패닝 트리 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/1197.%E2%80%85%EC%B5%9C%EC%86%8C%E2%80%85%EC%8A%A4%ED%8C%A8%EB%8B%9D%E2%80%85%ED%8A%B8%EB%A6%AC/README.md) |
| Baekjoon | 1237 | 정ㅋ벅ㅋ | Unrated | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Unrated/1237.%E2%80%85%EC%A0%95%E3%85%8B%EB%B2%85%E3%85%8B/README.md) |
| Baekjoon | 1259 | 팰린드롬수 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1259.%E2%80%85%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC%EC%88%98/README.md) |
| Baekjoon | 1271 | 엄청난 부자2 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1271.%E2%80%85%EC%97%84%EC%B2%AD%EB%82%9C%E2%80%85%EB%B6%80%EC%9E%902/README.md) |
| Baekjoon | 1316 | 그룹 단어 체커 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1316.%E2%80%85%EA%B7%B8%EB%A3%B9%E2%80%85%EB%8B%A8%EC%96%B4%E2%80%85%EC%B2%B4%EC%BB%A4/README.md) |
| Baekjoon | 1330 | 두 수 비교하기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1330.%E2%80%85%EB%91%90%E2%80%85%EC%88%98%E2%80%85%EB%B9%84%EA%B5%90%ED%95%98%EA%B8%B0/README.md) |
| Baekjoon | 1373 | 2진수 8진수 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1373.%E2%80%852%EC%A7%84%EC%88%98%E2%80%858%EC%A7%84%EC%88%98/README.md) |
| Baekjoon | 1380 | 귀걸이 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1380.%E2%80%85%EA%B7%80%EA%B1%B8%EC%9D%B4/README.md) |
| Baekjoon | 1402 | 아무래도이문제는A번난이도인것같다 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1402.%E2%80%85%EC%95%84%EB%AC%B4%EB%9E%98%EB%8F%84%EC%9D%B4%EB%AC%B8%EC%A0%9C%EB%8A%94A%EB%B2%88%EB%82%9C%EC%9D%B4%EB%8F%84%EC%9D%B8%EA%B2%83%EA%B0%99%EB%8B%A4/README.md) |
| Baekjoon | 1417 | 국회의원 선거 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1417.%E2%80%85%EA%B5%AD%ED%9A%8C%EC%9D%98%EC%9B%90%E2%80%85%EC%84%A0%EA%B1%B0/README.md) |
| Baekjoon | 1431 | 시리얼 번호 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1431.%E2%80%85%EC%8B%9C%EB%A6%AC%EC%96%BC%E2%80%85%EB%B2%88%ED%98%B8/README.md) |
| Baekjoon | 1436 | 영화감독 숌 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1436.%E2%80%85%EC%98%81%ED%99%94%EA%B0%90%EB%8F%85%E2%80%85%EC%88%8C/README.md) |
| Baekjoon | 1463 | 1로 만들기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1463.%E2%80%851%EB%A1%9C%E2%80%85%EB%A7%8C%EB%93%A4%EA%B8%B0/README.md) |
| Baekjoon | 1487 | 물건 팔기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1487.%E2%80%85%EB%AC%BC%EA%B1%B4%E2%80%85%ED%8C%94%EA%B8%B0/README.md) |
| Baekjoon | 1526 | 가장 큰 금민수 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1526.%E2%80%85%EA%B0%80%EC%9E%A5%E2%80%85%ED%81%B0%E2%80%85%EA%B8%88%EB%AF%BC%EC%88%98/README.md) |
| Baekjoon | 1546 | 평균 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1546.%E2%80%85%ED%8F%89%EA%B7%A0/README.md) |
| Baekjoon | 1620 | 나는야 포켓몬 마스터 이다솜 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1620.%E2%80%85%EB%82%98%EB%8A%94%EC%95%BC%E2%80%85%ED%8F%AC%EC%BC%93%EB%AA%AC%E2%80%85%EB%A7%88%EC%8A%A4%ED%84%B0%E2%80%85%EC%9D%B4%EB%8B%A4%EC%86%9C/README.md) |
| Baekjoon | 1629 | 곱셈 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1629.%E2%80%85%EA%B3%B1%EC%85%88/README.md) |
| Baekjoon | 1654 | 랜선 자르기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1654.%E2%80%85%EB%9E%9C%EC%84%A0%E2%80%85%EC%9E%90%EB%A5%B4%EA%B8%B0/README.md) |
| Baekjoon | 1676 | 팩토리얼 0의 개수 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1676.%E2%80%85%ED%8C%A9%ED%86%A0%EB%A6%AC%EC%96%BC%E2%80%850%EC%9D%98%E2%80%85%EA%B0%9C%EC%88%98/README.md) |
| Baekjoon | 1748 | 수 이어 쓰기 1 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1748.%E2%80%85%EC%88%98%E2%80%85%EC%9D%B4%EC%96%B4%E2%80%85%EC%93%B0%EA%B8%B0%E2%80%851/README.md) |
| Baekjoon | 1764 | 듣보잡 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1764.%E2%80%85%EB%93%A3%EB%B3%B4%EC%9E%A1/README.md) |
| Baekjoon | 1786 | 찾기 | Platinum | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Platinum/1786.%E2%80%85%EC%B0%BE%EA%B8%B0/README.md) |
| Baekjoon | 1787 | 문자열의 주기 예측 | Platinum | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Platinum/1787.%E2%80%85%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%98%E2%80%85%EC%A3%BC%EA%B8%B0%E2%80%85%EC%98%88%EC%B8%A1/README.md) |
| Baekjoon | 1812 | 사탕 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1812.%E2%80%85%EC%82%AC%ED%83%95/README.md) |
| Baekjoon | 1823 | 수확 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/1823.%E2%80%85%EC%88%98%ED%99%95/README.md) |
| Baekjoon | 1834 | 나머지와 몫이 같은 수 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1834.%E2%80%85%EB%82%98%EB%A8%B8%EC%A7%80%EC%99%80%E2%80%85%EB%AA%AB%EC%9D%B4%E2%80%85%EA%B0%99%EC%9D%80%E2%80%85%EC%88%98/README.md) |
| Baekjoon | 1850 | 최대공약수 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1850.%E2%80%85%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98/README.md) |
| Baekjoon | 1862 | 미터계 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1862.%E2%80%85%EB%AF%B8%ED%84%B0%EA%B3%84/README.md) |
| Baekjoon | 1874 | 스택 수열 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1874.%E2%80%85%EC%8A%A4%ED%83%9D%E2%80%85%EC%88%98%EC%97%B4/README.md) |
| Baekjoon | 1895 | 필터 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1895.%E2%80%85%ED%95%84%ED%84%B0/README.md) |
| Baekjoon | 1927 | 최소 힙 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1927.%E2%80%85%EC%B5%9C%EC%86%8C%E2%80%85%ED%9E%99/README.md) |
| Baekjoon | 1932 | 정수 삼각형 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1932.%E2%80%85%EC%A0%95%EC%88%98%E2%80%85%EC%82%BC%EA%B0%81%ED%98%95/README.md) |
| Baekjoon | 1940 | 주몽 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1940.%E2%80%85%EC%A3%BC%EB%AA%BD/README.md) |
| Baekjoon | 1978 | 소수 찾기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/1978.%E2%80%85%EC%86%8C%EC%88%98%E2%80%85%EC%B0%BE%EA%B8%B0/README.md) |
| Baekjoon | 1991 | 트리 순회 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/1991.%E2%80%85%ED%8A%B8%EB%A6%AC%E2%80%85%EC%88%9C%ED%9A%8C/README.md) |
| Baekjoon | 2028 | 자기복제수 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2028.%E2%80%85%EC%9E%90%EA%B8%B0%EB%B3%B5%EC%A0%9C%EC%88%98/README.md) |
| Baekjoon | 2072 | 오목 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2072.%E2%80%85%EC%98%A4%EB%AA%A9/README.md) |
| Baekjoon | 2075 | N번째 큰 수 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2075.%E2%80%85N%EB%B2%88%EC%A7%B8%E2%80%85%ED%81%B0%E2%80%85%EC%88%98/README.md) |
| Baekjoon | 2161 | 카드1 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2161.%E2%80%85%EC%B9%B4%EB%93%9C1/README.md) |
| Baekjoon | 2231 | 분해합 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2231.%E2%80%85%EB%B6%84%ED%95%B4%ED%95%A9/README.md) |
| Baekjoon | 2292 | 벌집 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2292.%E2%80%85%EB%B2%8C%EC%A7%91/README.md) |
| Baekjoon | 2312 | 수 복원하기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2312.%E2%80%85%EC%88%98%E2%80%85%EB%B3%B5%EC%9B%90%ED%95%98%EA%B8%B0/README.md) |
| Baekjoon | 2338 | 긴자리 계산 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2338.%E2%80%85%EA%B8%B4%EC%9E%90%EB%A6%AC%E2%80%85%EA%B3%84%EC%82%B0/README.md) |
| Baekjoon | 2346 | 풍선 터뜨리기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2346.%E2%80%85%ED%92%8D%EC%84%A0%E2%80%85%ED%84%B0%EB%9C%A8%EB%A6%AC%EA%B8%B0/README.md) |
| Baekjoon | 2393 | Rook | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2393.%E2%80%85Rook/README.md) |
| Baekjoon | 2420 | 사파리월드 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2420.%E2%80%85%EC%82%AC%ED%8C%8C%EB%A6%AC%EC%9B%94%EB%93%9C/README.md) |
| Baekjoon | 2438 | 별 찍기 － 1 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2438.%E2%80%85%EB%B3%84%E2%80%85%EC%B0%8D%EA%B8%B0%E2%80%85%EF%BC%8D%E2%80%851/README.md) |
| Baekjoon | 2439 | 별 찍기 － 2 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2439.%E2%80%85%EB%B3%84%E2%80%85%EC%B0%8D%EA%B8%B0%E2%80%85%EF%BC%8D%E2%80%852/README.md) |
| Baekjoon | 2475 | 검증수 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2475.%E2%80%85%EA%B2%80%EC%A6%9D%EC%88%98/README.md) |
| Baekjoon | 2491 | 수열 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2491.%E2%80%85%EC%88%98%EC%97%B4/README.md) |
| Baekjoon | 2501 | 약수 구하기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2501.%E2%80%85%EC%95%BD%EC%88%98%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0/README.md) |
| Baekjoon | 2512 | 예산 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2512.%E2%80%85%EC%98%88%EC%82%B0/README.md) |
| Baekjoon | 2535 | 아시아 정보올림피아드 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2535.%E2%80%85%EC%95%84%EC%8B%9C%EC%95%84%E2%80%85%EC%A0%95%EB%B3%B4%EC%98%AC%EB%A6%BC%ED%94%BC%EC%95%84%EB%93%9C/README.md) |
| Baekjoon | 2557 | Hello World | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2557.%E2%80%85Hello%E2%80%85World/README.md) |
| Baekjoon | 2558 | A＋B － 2 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2558.%E2%80%85A%EF%BC%8BB%E2%80%85%EF%BC%8D%E2%80%852/README.md) |
| Baekjoon | 2563 | 색종이 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2563.%E2%80%85%EC%83%89%EC%A2%85%EC%9D%B4/README.md) |
| Baekjoon | 2564 | 경비원 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2564.%E2%80%85%EA%B2%BD%EB%B9%84%EC%9B%90/README.md) |
| Baekjoon | 2579 | 계단 오르기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2579.%E2%80%85%EA%B3%84%EB%8B%A8%E2%80%85%EC%98%A4%EB%A5%B4%EA%B8%B0/README.md) |
| Baekjoon | 2588 | 곱셈 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2588.%E2%80%85%EA%B3%B1%EC%85%88/README.md) |
| Baekjoon | 2606 | 바이러스 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2606.%E2%80%85%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4/README.md) |
| Baekjoon | 2609 | 최대공약수와 최소공배수 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2609.%E2%80%85%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%99%80%E2%80%85%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98/README.md) |
| Baekjoon | 2738 | 행렬 덧셈 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2738.%E2%80%85%ED%96%89%EB%A0%AC%E2%80%85%EB%8D%A7%EC%85%88/README.md) |
| Baekjoon | 2739 | 구구단 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2739.%E2%80%85%EA%B5%AC%EA%B5%AC%EB%8B%A8/README.md) |
| Baekjoon | 2741 | N 찍기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2741.%E2%80%85N%E2%80%85%EC%B0%8D%EA%B8%B0/README.md) |
| Baekjoon | 2742 | 기찍 N | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2742.%E2%80%85%EA%B8%B0%EC%B0%8D%E2%80%85N/README.md) |
| Baekjoon | 2743 | 단어 길이 재기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2743.%E2%80%85%EB%8B%A8%EC%96%B4%E2%80%85%EA%B8%B8%EC%9D%B4%E2%80%85%EC%9E%AC%EA%B8%B0/README.md) |
| Baekjoon | 2744 | 대소문자 바꾸기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2744.%E2%80%85%EB%8C%80%EC%86%8C%EB%AC%B8%EC%9E%90%E2%80%85%EB%B0%94%EA%BE%B8%EA%B8%B0/README.md) |
| Baekjoon | 2750 | 수 정렬하기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2750.%E2%80%85%EC%88%98%E2%80%85%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0/README.md) |
| Baekjoon | 2751 | 수 정렬하기 2 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2751.%E2%80%85%EC%88%98%E2%80%85%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0%E2%80%852/README.md) |
| Baekjoon | 2753 | 윤년 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2753.%E2%80%85%EC%9C%A4%EB%85%84/README.md) |
| Baekjoon | 2754 | 학점계산 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2754.%E2%80%85%ED%95%99%EC%A0%90%EA%B3%84%EC%82%B0/README.md) |
| Baekjoon | 2775 | 부녀회장이 될테야 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2775.%E2%80%85%EB%B6%80%EB%85%80%ED%9A%8C%EC%9E%A5%EC%9D%B4%E2%80%85%EB%90%A0%ED%85%8C%EC%95%BC/README.md) |
| Baekjoon | 2783 | 삼각 김밥 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2783.%E2%80%85%EC%82%BC%EA%B0%81%E2%80%85%EA%B9%80%EB%B0%A5/README.md) |
| Baekjoon | 2798 | 블랙잭 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2798.%E2%80%85%EB%B8%94%EB%9E%99%EC%9E%AD/README.md) |
| Baekjoon | 2805 | 나무 자르기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2805.%E2%80%85%EB%82%98%EB%AC%B4%E2%80%85%EC%9E%90%EB%A5%B4%EA%B8%B0/README.md) |
| Baekjoon | 2822 | 점수 계산 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2822.%E2%80%85%EC%A0%90%EC%88%98%E2%80%85%EA%B3%84%EC%82%B0/README.md) |
| Baekjoon | 2839 | 설탕 배달 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2839.%E2%80%85%EC%84%A4%ED%83%95%E2%80%85%EB%B0%B0%EB%8B%AC/README.md) |
| Baekjoon | 2869 | 달팽이는 올라가고 싶다 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2869.%E2%80%85%EB%8B%AC%ED%8C%BD%EC%9D%B4%EB%8A%94%E2%80%85%EC%98%AC%EB%9D%BC%EA%B0%80%EA%B3%A0%E2%80%85%EC%8B%B6%EB%8B%A4/README.md) |
| Baekjoon | 2910 | 빈도 정렬 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2910.%E2%80%85%EB%B9%88%EB%8F%84%E2%80%85%EC%A0%95%EB%A0%AC/README.md) |
| Baekjoon | 2960 | 에라토스테네스의 체 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2960.%E2%80%85%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98%E2%80%85%EC%B2%B4/README.md) |
| Baekjoon | 2966 | 찍기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/2966.%E2%80%85%EC%B0%8D%EA%B8%B0/README.md) |
| Baekjoon | 2992 | 크면서 작은 수 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/2992.%E2%80%85%ED%81%AC%EB%A9%B4%EC%84%9C%E2%80%85%EC%9E%91%EC%9D%80%E2%80%85%EC%88%98/README.md) |
| Baekjoon | 3003 | 킹， 퀸， 룩， 비숍， 나이트， 폰 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/3003.%E2%80%85%ED%82%B9%EF%BC%8C%E2%80%85%ED%80%B8%EF%BC%8C%E2%80%85%EB%A3%A9%EF%BC%8C%E2%80%85%EB%B9%84%EC%88%8D%EF%BC%8C%E2%80%85%EB%82%98%EC%9D%B4%ED%8A%B8%EF%BC%8C%E2%80%85%ED%8F%B0/README.md) |
| Baekjoon | 3004 | 체스판 조각 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/3004.%E2%80%85%EC%B2%B4%EC%8A%A4%ED%8C%90%E2%80%85%EC%A1%B0%EA%B0%81/README.md) |
| Baekjoon | 3052 | 나머지 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/3052.%E2%80%85%EB%82%98%EB%A8%B8%EC%A7%80/README.md) |
| Baekjoon | 3098 | 소셜네트워크 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/3098.%E2%80%85%EC%86%8C%EC%85%9C%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC/README.md) |
| Baekjoon | 3733 | Shares | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/3733.%E2%80%85Shares/README.md) |
| Baekjoon | 3779 | 주기 | Platinum | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Platinum/3779.%E2%80%85%EC%A3%BC%EA%B8%B0/README.md) |
| Baekjoon | 3991 | 한번 쏘면 멈출 수 없어 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/3991.%E2%80%85%ED%95%9C%EB%B2%88%E2%80%85%EC%8F%98%EB%A9%B4%E2%80%85%EB%A9%88%EC%B6%9C%E2%80%85%EC%88%98%E2%80%85%EC%97%86%EC%96%B4/README.md) |
| Baekjoon | 4101 | 크냐？ | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/4101.%E2%80%85%ED%81%AC%EB%83%90%EF%BC%9F/README.md) |
| Baekjoon | 4118 | Fred’s Lotto Tickets | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/4118.%E2%80%85Fred%E2%80%99s%E2%80%85Lotto%E2%80%85Tickets/README.md) |
| Baekjoon | 4141 | Numbersrebmun | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/4141.%E2%80%85Numbersrebmun/README.md) |
| Baekjoon | 4153 | 직각삼각형 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/4153.%E2%80%85%EC%A7%81%EA%B0%81%EC%82%BC%EA%B0%81%ED%98%95/README.md) |
| Baekjoon | 4354 | 문자열 제곱 | Platinum | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Platinum/4354.%E2%80%85%EB%AC%B8%EC%9E%90%EC%97%B4%E2%80%85%EC%A0%9C%EA%B3%B1/README.md) |
| Baekjoon | 4378 | 트ㅏㅊ； | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/4378.%E2%80%85%ED%8A%B8%E3%85%8F%E3%85%8A%EF%BC%9B/README.md) |
| Baekjoon | 4454 | 상근이의 여자친구 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/4454.%E2%80%85%EC%83%81%EA%B7%BC%EC%9D%B4%EC%9D%98%E2%80%85%EC%97%AC%EC%9E%90%EC%B9%9C%EA%B5%AC/README.md) |
| Baekjoon | 4697 | Fifty Coats of Gray | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/4697.%E2%80%85Fifty%E2%80%85Coats%E2%80%85of%E2%80%85Gray/README.md) |
| Baekjoon | 4909 | Judging Olympia | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/4909.%E2%80%85Judging%E2%80%85Olympia/README.md) |
| Baekjoon | 5052 | 전화번호 목록 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/5052.%E2%80%85%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8%E2%80%85%EB%AA%A9%EB%A1%9D/README.md) |
| Baekjoon | 5054 | 주차의 신 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/5054.%E2%80%85%EC%A3%BC%EC%B0%A8%EC%9D%98%E2%80%85%EC%8B%A0/README.md) |
| Baekjoon | 5337 | 웰컴 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/5337.%E2%80%85%EC%9B%B0%EC%BB%B4/README.md) |
| Baekjoon | 5341 | Pyramids | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/5341.%E2%80%85Pyramids/README.md) |
| Baekjoon | 5393 | Collatz | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/5393.%E2%80%85Collatz/README.md) |
| Baekjoon | 5533 | 유니크 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/5533.%E2%80%85%EC%9C%A0%EB%8B%88%ED%81%AC/README.md) |
| Baekjoon | 5556 | 타일 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/5556.%E2%80%85%ED%83%80%EC%9D%BC/README.md) |
| Baekjoon | 5623 | 수열의 합 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/5623.%E2%80%85%EC%88%98%EC%97%B4%EC%9D%98%E2%80%85%ED%95%A9/README.md) |
| Baekjoon | 5670 | 휴대폰 자판 | Platinum | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Platinum/5670.%E2%80%85%ED%9C%B4%EB%8C%80%ED%8F%B0%E2%80%85%EC%9E%90%ED%8C%90/README.md) |
| Baekjoon | 5671 | 호텔 방 번호 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/5671.%E2%80%85%ED%98%B8%ED%85%94%E2%80%85%EB%B0%A9%E2%80%85%EB%B2%88%ED%98%B8/README.md) |
| Baekjoon | 5988 | 홀수일까 짝수일까 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/5988.%E2%80%85%ED%99%80%EC%88%98%EC%9D%BC%EA%B9%8C%E2%80%85%EC%A7%9D%EC%88%98%EC%9D%BC%EA%B9%8C/README.md) |
| Baekjoon | 6260 | Encrypted SMS | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/6260.%E2%80%85Encrypted%E2%80%85SMS/README.md) |
| Baekjoon | 6884 | 소수 부분 수열 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/6884.%E2%80%85%EC%86%8C%EC%88%98%E2%80%85%EB%B6%80%EB%B6%84%E2%80%85%EC%88%98%EC%97%B4/README.md) |
| Baekjoon | 6996 | 애너그램 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/6996.%E2%80%85%EC%95%A0%EB%84%88%EA%B7%B8%EB%9E%A8/README.md) |
| Baekjoon | 7489 | 팩토리얼 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/7489.%E2%80%85%ED%8C%A9%ED%86%A0%EB%A6%AC%EC%96%BC/README.md) |
| Baekjoon | 7567 | 그릇 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/7567.%E2%80%85%EA%B7%B8%EB%A6%87/README.md) |
| Baekjoon | 7568 | 덩치 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/7568.%E2%80%85%EB%8D%A9%EC%B9%98/README.md) |
| Baekjoon | 7572 | 간지（干支） | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/7572.%E2%80%85%EA%B0%84%EC%A7%80%EF%BC%88%E5%B9%B2%E6%94%AF%EF%BC%89/README.md) |
| Baekjoon | 7576 | 토마토 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/7576.%E2%80%85%ED%86%A0%EB%A7%88%ED%86%A0/README.md) |
| Baekjoon | 8370 | Plane | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/8370.%E2%80%85Plane/README.md) |
| Baekjoon | 8393 | 합 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/8393.%E2%80%85%ED%95%A9/README.md) |
| Baekjoon | 8394 | 악수 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/8394.%E2%80%85%EC%95%85%EC%88%98/README.md) |
| Baekjoon | 8974 | 희주의 수학시험 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/8974.%E2%80%85%ED%9D%AC%EC%A3%BC%EC%9D%98%E2%80%85%EC%88%98%ED%95%99%EC%8B%9C%ED%97%98/README.md) |
| Baekjoon | 9095 | 1， 2， 3 더하기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/9095.%E2%80%851%EF%BC%8C%E2%80%852%EF%BC%8C%E2%80%853%E2%80%85%EB%8D%94%ED%95%98%EA%B8%B0/README.md) |
| Baekjoon | 9366 | 삼각형 분류 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/9366.%E2%80%85%EC%82%BC%EA%B0%81%ED%98%95%E2%80%85%EB%B6%84%EB%A5%98/README.md) |
| Baekjoon | 9375 | 패션왕 신해빈 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/9375.%E2%80%85%ED%8C%A8%EC%85%98%EC%99%95%E2%80%85%EC%8B%A0%ED%95%B4%EB%B9%88/README.md) |
| Baekjoon | 9461 | 파도반 수열 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/9461.%E2%80%85%ED%8C%8C%EB%8F%84%EB%B0%98%E2%80%85%EC%88%98%EC%97%B4/README.md) |
| Baekjoon | 9465 | 스티커 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/9465.%E2%80%85%EC%8A%A4%ED%8B%B0%EC%BB%A4/README.md) |
| Baekjoon | 9498 | 시험 성적 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/9498.%E2%80%85%EC%8B%9C%ED%97%98%E2%80%85%EC%84%B1%EC%A0%81/README.md) |
| Baekjoon | 9536 | 여우는 어떻게 울지？ | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/9536.%E2%80%85%EC%97%AC%EC%9A%B0%EB%8A%94%E2%80%85%EC%96%B4%EB%96%BB%EA%B2%8C%E2%80%85%EC%9A%B8%EC%A7%80%EF%BC%9F/README.md) |
| Baekjoon | 9625 | BABBA | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/9625.%E2%80%85BABBA/README.md) |
| Baekjoon | 9742 | 순열 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/9742.%E2%80%85%EC%88%9C%EC%97%B4/README.md) |
| Baekjoon | 10171 | 고양이 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10171.%E2%80%85%EA%B3%A0%EC%96%91%EC%9D%B4/README.md) |
| Baekjoon | 10172 | 개 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10172.%E2%80%85%EA%B0%9C/README.md) |
| Baekjoon | 10189 | Hook | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10189.%E2%80%85Hook/README.md) |
| Baekjoon | 10420 | 기념일 1 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10420.%E2%80%85%EA%B8%B0%EB%85%90%EC%9D%BC%E2%80%851/README.md) |
| Baekjoon | 10430 | 나머지 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10430.%E2%80%85%EB%82%98%EB%A8%B8%EC%A7%80/README.md) |
| Baekjoon | 10469 | 사이 나쁜 여왕들 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/10469.%E2%80%85%EC%82%AC%EC%9D%B4%E2%80%85%EB%82%98%EC%81%9C%E2%80%85%EC%97%AC%EC%99%95%EB%93%A4/README.md) |
| Baekjoon | 10728 | XOR삼형제 1 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/10728.%E2%80%85XOR%EC%82%BC%ED%98%95%EC%A0%9C%E2%80%851/README.md) |
| Baekjoon | 10809 | 알파벳 찾기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10809.%E2%80%85%EC%95%8C%ED%8C%8C%EB%B2%B3%E2%80%85%EC%B0%BE%EA%B8%B0/README.md) |
| Baekjoon | 10811 | 바구니 뒤집기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10811.%E2%80%85%EB%B0%94%EA%B5%AC%EB%8B%88%E2%80%85%EB%92%A4%EC%A7%91%EA%B8%B0/README.md) |
| Baekjoon | 10814 | 나이순 정렬 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/10814.%E2%80%85%EB%82%98%EC%9D%B4%EC%88%9C%E2%80%85%EC%A0%95%EB%A0%AC/README.md) |
| Baekjoon | 10817 | 세 수 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10817.%E2%80%85%EC%84%B8%E2%80%85%EC%88%98/README.md) |
| Baekjoon | 10828 | 스택 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/10828.%E2%80%85%EC%8A%A4%ED%83%9D/README.md) |
| Baekjoon | 10845 | 큐 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/10845.%E2%80%85%ED%81%90/README.md) |
| Baekjoon | 10864 | 친구 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10864.%E2%80%85%EC%B9%9C%EA%B5%AC/README.md) |
| Baekjoon | 10866 | 덱 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/10866.%E2%80%85%EB%8D%B1/README.md) |
| Baekjoon | 10869 | 사칙연산 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10869.%E2%80%85%EC%82%AC%EC%B9%99%EC%97%B0%EC%82%B0/README.md) |
| Baekjoon | 10871 | X보다 작은 수 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10871.%E2%80%85X%EB%B3%B4%EB%8B%A4%E2%80%85%EC%9E%91%EC%9D%80%E2%80%85%EC%88%98/README.md) |
| Baekjoon | 10892 | Divide into triangle | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/10892.%E2%80%85Divide%E2%80%85into%E2%80%85triangle/README.md) |
| Baekjoon | 10926 | ？？！ | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10926.%E2%80%85%EF%BC%9F%EF%BC%9F%EF%BC%81/README.md) |
| Baekjoon | 10950 | A＋B － 3 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10950.%E2%80%85A%EF%BC%8BB%E2%80%85%EF%BC%8D%E2%80%853/README.md) |
| Baekjoon | 10951 | A＋B － 4 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10951.%E2%80%85A%EF%BC%8BB%E2%80%85%EF%BC%8D%E2%80%854/README.md) |
| Baekjoon | 10952 | A＋B － 5 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10952.%E2%80%85A%EF%BC%8BB%E2%80%85%EF%BC%8D%E2%80%855/README.md) |
| Baekjoon | 10953 | A＋B － 6 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10953.%E2%80%85A%EF%BC%8BB%E2%80%85%EF%BC%8D%E2%80%856/README.md) |
| Baekjoon | 10989 | 수 정렬하기 3 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10989.%E2%80%85%EC%88%98%E2%80%85%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0%E2%80%853/README.md) |
| Baekjoon | 10998 | A×B | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/10998.%E2%80%85A%C3%97B/README.md) |
| Baekjoon | 11022 | A＋B － 8 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/11022.%E2%80%85A%EF%BC%8BB%E2%80%85%EF%BC%8D%E2%80%858/README.md) |
| Baekjoon | 11047 | 동전 0 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/11047.%E2%80%85%EB%8F%99%EC%A0%84%E2%80%850/README.md) |
| Baekjoon | 11050 | 이항 계수 1 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/11050.%E2%80%85%EC%9D%B4%ED%95%AD%E2%80%85%EA%B3%84%EC%88%98%E2%80%851/README.md) |
| Baekjoon | 11053 | 가장 긴 증가하는 부분 수열 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/11053.%E2%80%85%EA%B0%80%EC%9E%A5%E2%80%85%EA%B8%B4%E2%80%85%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94%E2%80%85%EB%B6%80%EB%B6%84%E2%80%85%EC%88%98%EC%97%B4/README.md) |
| Baekjoon | 11068 | 회문인 수 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/11068.%E2%80%85%ED%9A%8C%EB%AC%B8%EC%9D%B8%E2%80%85%EC%88%98/README.md) |
| Baekjoon | 11279 | 최대 힙 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/11279.%E2%80%85%EC%B5%9C%EB%8C%80%E2%80%85%ED%9E%99/README.md) |
| Baekjoon | 11320 | 삼각 무늬 － 1 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/11320.%E2%80%85%EC%82%BC%EA%B0%81%E2%80%85%EB%AC%B4%EB%8A%AC%E2%80%85%EF%BC%8D%E2%80%851/README.md) |
| Baekjoon | 11382 | 꼬마 정민 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/11382.%E2%80%85%EA%BC%AC%EB%A7%88%E2%80%85%EC%A0%95%EB%AF%BC/README.md) |
| Baekjoon | 11399 | ATM | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/11399.%E2%80%85ATM/README.md) |
| Baekjoon | 11578 | 팀원 모집 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/11578.%E2%80%85%ED%8C%80%EC%9B%90%E2%80%85%EB%AA%A8%EC%A7%91/README.md) |
| Baekjoon | 11650 | 좌표 정렬하기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/11650.%E2%80%85%EC%A2%8C%ED%91%9C%E2%80%85%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0/README.md) |
| Baekjoon | 11654 | 아스키 코드 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/11654.%E2%80%85%EC%95%84%EC%8A%A4%ED%82%A4%E2%80%85%EC%BD%94%EB%93%9C/README.md) |
| Baekjoon | 11659 | 구간 합 구하기 4 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/11659.%E2%80%85%EA%B5%AC%EA%B0%84%E2%80%85%ED%95%A9%E2%80%85%EA%B5%AC%ED%95%98%EA%B8%B0%E2%80%854/README.md) |
| Baekjoon | 11720 | 숫자의 합 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/11720.%E2%80%85%EC%88%AB%EC%9E%90%EC%9D%98%E2%80%85%ED%95%A9/README.md) |
| Baekjoon | 11723 | 집합 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/11723.%E2%80%85%EC%A7%91%ED%95%A9/README.md) |
| Baekjoon | 11725 | 트리의 부모 찾기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/11725.%E2%80%85%ED%8A%B8%EB%A6%AC%EC%9D%98%E2%80%85%EB%B6%80%EB%AA%A8%E2%80%85%EC%B0%BE%EA%B8%B0/README.md) |
| Baekjoon | 11726 | 2×n 타일링 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/11726.%E2%80%852%C3%97n%E2%80%85%ED%83%80%EC%9D%BC%EB%A7%81/README.md) |
| Baekjoon | 11727 | 2×n 타일링 2 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/11727.%E2%80%852%C3%97n%E2%80%85%ED%83%80%EC%9D%BC%EB%A7%81%E2%80%852/README.md) |
| Baekjoon | 11944 | NN | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/11944.%E2%80%85NN/README.md) |
| Baekjoon | 12789 | 도키도키 간식드리미 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/12789.%E2%80%85%EB%8F%84%ED%82%A4%EB%8F%84%ED%82%A4%E2%80%85%EA%B0%84%EC%8B%9D%EB%93%9C%EB%A6%AC%EB%AF%B8/README.md) |
| Baekjoon | 12847 | 꿀 아르바이트 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/12847.%E2%80%85%EA%BF%80%E2%80%85%EC%95%84%EB%A5%B4%EB%B0%94%EC%9D%B4%ED%8A%B8/README.md) |
| Baekjoon | 13305 | 주유소 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/13305.%E2%80%85%EC%A3%BC%EC%9C%A0%EC%86%8C/README.md) |
| Baekjoon | 13413 | 오셀로 재배치 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/13413.%E2%80%85%EC%98%A4%EC%85%80%EB%A1%9C%E2%80%85%EC%9E%AC%EB%B0%B0%EC%B9%98/README.md) |
| Baekjoon | 13419 | 탕수육 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/13419.%E2%80%85%ED%83%95%EC%88%98%EC%9C%A1/README.md) |
| Baekjoon | 13706 | 제곱근 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/13706.%E2%80%85%EC%A0%9C%EA%B3%B1%EA%B7%BC/README.md) |
| Baekjoon | 13923 | 오버워치 월드컵 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/13923.%E2%80%85%EC%98%A4%EB%B2%84%EC%9B%8C%EC%B9%98%E2%80%85%EC%9B%94%EB%93%9C%EC%BB%B5/README.md) |
| Baekjoon | 14039 | Magic Squares | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/14039.%E2%80%85Magic%E2%80%85Squares/README.md) |
| Baekjoon | 14043 | Ragaman | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/14043.%E2%80%85Ragaman/README.md) |
| Baekjoon | 14225 | 부분수열의 합 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/14225.%E2%80%85%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4%EC%9D%98%E2%80%85%ED%95%A9/README.md) |
| Baekjoon | 14246 | K보다 큰 구간 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/14246.%E2%80%85K%EB%B3%B4%EB%8B%A4%E2%80%85%ED%81%B0%E2%80%85%EA%B5%AC%EA%B0%84/README.md) |
| Baekjoon | 14292 | Beautiful Numbers （Small） | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/14292.%E2%80%85Beautiful%E2%80%85Numbers%E2%80%85%EF%BC%88Small%EF%BC%89/README.md) |
| Baekjoon | 14539 | Grid Pattern | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/14539.%E2%80%85Grid%E2%80%85Pattern/README.md) |
| Baekjoon | 14607 | 피자 （Large） | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/14607.%E2%80%85%ED%94%BC%EC%9E%90%E2%80%85%EF%BC%88Large%EF%BC%89/README.md) |
| Baekjoon | 14626 | ISBN | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/14626.%E2%80%85ISBN/README.md) |
| Baekjoon | 14627 | 파닭파닭 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/14627.%E2%80%85%ED%8C%8C%EB%8B%AD%ED%8C%8C%EB%8B%AD/README.md) |
| Baekjoon | 14681 | 사분면 고르기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/14681.%E2%80%85%EC%82%AC%EB%B6%84%EB%A9%B4%E2%80%85%EA%B3%A0%EB%A5%B4%EA%B8%B0/README.md) |
| Baekjoon | 14725 | 개미굴 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/14725.%E2%80%85%EA%B0%9C%EB%AF%B8%EA%B5%B4/README.md) |
| Baekjoon | 14910 | 오르막 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/14910.%E2%80%85%EC%98%A4%EB%A5%B4%EB%A7%89/README.md) |
| Baekjoon | 14924 | 폰 노이만과 파리 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/14924.%E2%80%85%ED%8F%B0%E2%80%85%EB%85%B8%EC%9D%B4%EB%A7%8C%EA%B3%BC%E2%80%85%ED%8C%8C%EB%A6%AC/README.md) |
| Baekjoon | 14929 | 귀찮아 （SIB） | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/14929.%E2%80%85%EA%B7%80%EC%B0%AE%EC%95%84%E2%80%85%EF%BC%88SIB%EF%BC%89/README.md) |
| Baekjoon | 15439 | 베라의 패션 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/15439.%E2%80%85%EB%B2%A0%EB%9D%BC%EC%9D%98%E2%80%85%ED%8C%A8%EC%85%98/README.md) |
| Baekjoon | 15489 | 파스칼 삼각형 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/15489.%E2%80%85%ED%8C%8C%EC%8A%A4%EC%B9%BC%E2%80%85%EC%82%BC%EA%B0%81%ED%98%95/README.md) |
| Baekjoon | 15549 | if | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/15549.%E2%80%85if/README.md) |
| Baekjoon | 15650 | N과 M （2） | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/15650.%E2%80%85N%EA%B3%BC%E2%80%85M%E2%80%85%EF%BC%882%EF%BC%89/README.md) |
| Baekjoon | 15651 | N과 M （3） | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/15651.%E2%80%85N%EA%B3%BC%E2%80%85M%E2%80%85%EF%BC%883%EF%BC%89/README.md) |
| Baekjoon | 15652 | N과 M （4） | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/15652.%E2%80%85N%EA%B3%BC%E2%80%85M%E2%80%85%EF%BC%884%EF%BC%89/README.md) |
| Baekjoon | 15654 | N과 M （5） | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/15654.%E2%80%85N%EA%B3%BC%E2%80%85M%E2%80%85%EF%BC%885%EF%BC%89/README.md) |
| Baekjoon | 15655 | N과 M （6） | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/15655.%E2%80%85N%EA%B3%BC%E2%80%85M%E2%80%85%EF%BC%886%EF%BC%89/README.md) |
| Baekjoon | 15663 | N과 M （9） | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/15663.%E2%80%85N%EA%B3%BC%E2%80%85M%E2%80%85%EF%BC%889%EF%BC%89/README.md) |
| Baekjoon | 15666 | N과 M （12） | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/15666.%E2%80%85N%EA%B3%BC%E2%80%85M%E2%80%85%EF%BC%8812%EF%BC%89/README.md) |
| Baekjoon | 15680 | 연세대학교 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/15680.%E2%80%85%EC%97%B0%EC%84%B8%EB%8C%80%ED%95%99%EA%B5%90/README.md) |
| Baekjoon | 15700 | 타일 채우기 4 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/15700.%E2%80%85%ED%83%80%EC%9D%BC%E2%80%85%EC%B1%84%EC%9A%B0%EA%B8%B0%E2%80%854/README.md) |
| Baekjoon | 15727 | 조별과제를 하려는데 조장이 사라졌다 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/15727.%E2%80%85%EC%A1%B0%EB%B3%84%EA%B3%BC%EC%A0%9C%EB%A5%BC%E2%80%85%ED%95%98%EB%A0%A4%EB%8A%94%EB%8D%B0%E2%80%85%EC%A1%B0%EC%9E%A5%EC%9D%B4%E2%80%85%EC%82%AC%EB%9D%BC%EC%A1%8C%EB%8B%A4/README.md) |
| Baekjoon | 15740 | A＋B － 9 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/15740.%E2%80%85A%EF%BC%8BB%E2%80%85%EF%BC%8D%E2%80%859/README.md) |
| Baekjoon | 15786 | Send me the money | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/15786.%E2%80%85Send%E2%80%85me%E2%80%85the%E2%80%85money/README.md) |
| Baekjoon | 15818 | 오버플로우와 모듈러 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/15818.%E2%80%85%EC%98%A4%EB%B2%84%ED%94%8C%EB%A1%9C%EC%9A%B0%EC%99%80%E2%80%85%EB%AA%A8%EB%93%88%EB%9F%AC/README.md) |
| Baekjoon | 15821 | 낚이고 낚아라 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/15821.%E2%80%85%EB%82%9A%EC%9D%B4%EA%B3%A0%E2%80%85%EB%82%9A%EC%95%84%EB%9D%BC/README.md) |
| Baekjoon | 15829 | Hashing | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/15829.%E2%80%85Hashing/README.md) |
| Baekjoon | 15836 | Matrix Multiplication Calculator | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/15836.%E2%80%85Matrix%E2%80%85Multiplication%E2%80%85Calculator/README.md) |
| Baekjoon | 15964 | 이상한 기호 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/15964.%E2%80%85%EC%9D%B4%EC%83%81%ED%95%9C%E2%80%85%EA%B8%B0%ED%98%B8/README.md) |
| Baekjoon | 15990 | 1， 2， 3 더하기 5 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/15990.%E2%80%851%EF%BC%8C%E2%80%852%EF%BC%8C%E2%80%853%E2%80%85%EB%8D%94%ED%95%98%EA%B8%B0%E2%80%855/README.md) |
| Baekjoon | 16162 | 가희와 3단 고음 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/16162.%E2%80%85%EA%B0%80%ED%9D%AC%EC%99%80%E2%80%853%EB%8B%A8%E2%80%85%EA%B3%A0%EC%9D%8C/README.md) |
| Baekjoon | 16171 | 나는 친구가 적다 （Small） | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/16171.%E2%80%85%EB%82%98%EB%8A%94%E2%80%85%EC%B9%9C%EA%B5%AC%EA%B0%80%E2%80%85%EC%A0%81%EB%8B%A4%E2%80%85%EF%BC%88Small%EF%BC%89/README.md) |
| Baekjoon | 16283 | Farm | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/16283.%E2%80%85Farm/README.md) |
| Baekjoon | 16497 | 대출 요청 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/16497.%E2%80%85%EB%8C%80%EC%B6%9C%E2%80%85%EC%9A%94%EC%B2%AD/README.md) |
| Baekjoon | 16567 | 바이너리 왕국 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/16567.%E2%80%85%EB%B0%94%EC%9D%B4%EB%84%88%EB%A6%AC%E2%80%85%EC%99%95%EA%B5%AD/README.md) |
| Baekjoon | 16715 | Inspiration | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/16715.%E2%80%85Inspiration/README.md) |
| Baekjoon | 16922 | 로마 숫자 만들기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/16922.%E2%80%85%EB%A1%9C%EB%A7%88%E2%80%85%EC%88%AB%EC%9E%90%E2%80%85%EB%A7%8C%EB%93%A4%EA%B8%B0/README.md) |
| Baekjoon | 16934 | 게임 닉네임 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/16934.%E2%80%85%EA%B2%8C%EC%9E%84%E2%80%85%EB%8B%89%EB%84%A4%EC%9E%84/README.md) |
| Baekjoon | 16948 | 데스 나이트 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/16948.%E2%80%85%EB%8D%B0%EC%8A%A4%E2%80%85%EB%82%98%EC%9D%B4%ED%8A%B8/README.md) |
| Baekjoon | 16951 | 블록 놀이 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/16951.%E2%80%85%EB%B8%94%EB%A1%9D%E2%80%85%EB%86%80%EC%9D%B4/README.md) |
| Baekjoon | 16953 | A → B | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/16953.%E2%80%85A%E2%80%85%E2%86%92%E2%80%85B/README.md) |
| Baekjoon | 16960 | 스위치와 램프 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/16960.%E2%80%85%EC%8A%A4%EC%9C%84%EC%B9%98%EC%99%80%E2%80%85%EB%9E%A8%ED%94%84/README.md) |
| Baekjoon | 17086 | 아기 상어 2 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/17086.%E2%80%85%EC%95%84%EA%B8%B0%E2%80%85%EC%83%81%EC%96%B4%E2%80%852/README.md) |
| Baekjoon | 17219 | 비밀번호 찾기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/17219.%E2%80%85%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8%E2%80%85%EC%B0%BE%EA%B8%B0/README.md) |
| Baekjoon | 17273 | 카드 공장 （Small） | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/17273.%E2%80%85%EC%B9%B4%EB%93%9C%E2%80%85%EA%B3%B5%EC%9E%A5%E2%80%85%EF%BC%88Small%EF%BC%89/README.md) |
| Baekjoon | 17284 | Vending Machine | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/17284.%E2%80%85Vending%E2%80%85Machine/README.md) |
| Baekjoon | 17294 | 귀여운 수～ε٩（๑＞ ₃ ＜）۶з | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/17294.%E2%80%85%EA%B7%80%EC%97%AC%EC%9A%B4%E2%80%85%EC%88%98%EF%BD%9E%CE%B5%D9%A9%EF%BC%88%E0%B9%91%EF%BC%9E%E2%80%85%E2%82%83%E2%80%85%EF%BC%9C%EF%BC%89%DB%B6%D0%B7/README.md) |
| Baekjoon | 17479 | 정식당 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/17479.%E2%80%85%EC%A0%95%EC%8B%9D%EB%8B%B9/README.md) |
| Baekjoon | 17609 | 회문 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/17609.%E2%80%85%ED%9A%8C%EB%AC%B8/README.md) |
| Baekjoon | 17626 | Four Squares | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/17626.%E2%80%85Four%E2%80%85Squares/README.md) |
| Baekjoon | 17826 | 나의 학점은？ | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/17826.%E2%80%85%EB%82%98%EC%9D%98%E2%80%85%ED%95%99%EC%A0%90%EC%9D%80%EF%BC%9F/README.md) |
| Baekjoon | 17843 | 시계 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/17843.%E2%80%85%EC%8B%9C%EA%B3%84/README.md) |
| Baekjoon | 18108 | 1998년생인 내가 태국에서는 2541년생？！ | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/18108.%E2%80%851998%EB%85%84%EC%83%9D%EC%9D%B8%E2%80%85%EB%82%B4%EA%B0%80%E2%80%85%ED%83%9C%EA%B5%AD%EC%97%90%EC%84%9C%EB%8A%94%E2%80%852541%EB%85%84%EC%83%9D%EF%BC%9F%EF%BC%81/README.md) |
| Baekjoon | 18111 | 마인크래프트 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/18111.%E2%80%85%EB%A7%88%EC%9D%B8%ED%81%AC%EB%9E%98%ED%94%84%ED%8A%B8/README.md) |
| Baekjoon | 18129 | 이상한 암호코드 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/18129.%E2%80%85%EC%9D%B4%EC%83%81%ED%95%9C%E2%80%85%EC%95%94%ED%98%B8%EC%BD%94%EB%93%9C/README.md) |
| Baekjoon | 18301 | Rats | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/18301.%E2%80%85Rats/README.md) |
| Baekjoon | 18511 | 큰 수 구성하기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/18511.%E2%80%85%ED%81%B0%E2%80%85%EC%88%98%E2%80%85%EA%B5%AC%EC%84%B1%ED%95%98%EA%B8%B0/README.md) |
| Baekjoon | 18512 | 점프 점프 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/18512.%E2%80%85%EC%A0%90%ED%94%84%E2%80%85%EC%A0%90%ED%94%84/README.md) |
| Baekjoon | 18795 | 이동하기 3 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/18795.%E2%80%85%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0%E2%80%853/README.md) |
| Baekjoon | 19829 | The Pleasant Walk | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/19829.%E2%80%85The%E2%80%85Pleasant%E2%80%85Walk/README.md) |
| Baekjoon | 19944 | 뉴비의 기준은 뭘까？ | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/19944.%E2%80%85%EB%89%B4%EB%B9%84%EC%9D%98%E2%80%85%EA%B8%B0%EC%A4%80%EC%9D%80%E2%80%85%EB%AD%98%EA%B9%8C%EF%BC%9F/README.md) |
| Baekjoon | 19947 | 투자의 귀재 배주형 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/19947.%E2%80%85%ED%88%AC%EC%9E%90%EC%9D%98%E2%80%85%EA%B7%80%EC%9E%AC%E2%80%85%EB%B0%B0%EC%A3%BC%ED%98%95/README.md) |
| Baekjoon | 20115 | 에너지 드링크 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/20115.%E2%80%85%EC%97%90%EB%84%88%EC%A7%80%E2%80%85%EB%93%9C%EB%A7%81%ED%81%AC/README.md) |
| Baekjoon | 20124 | 모르고리즘 회장님 추천 받습니다 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/20124.%E2%80%85%EB%AA%A8%EB%A5%B4%EA%B3%A0%EB%A6%AC%EC%A6%98%E2%80%85%ED%9A%8C%EC%9E%A5%EB%8B%98%E2%80%85%EC%B6%94%EC%B2%9C%E2%80%85%EB%B0%9B%EC%8A%B5%EB%8B%88%EB%8B%A4/README.md) |
| Baekjoon | 20153 | 영웅이는 2의 거듭 제곱을 좋아해！ 영웅이는 2의 거듭 제곱을 좋아해！ | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/20153.%E2%80%85%EC%98%81%EC%9B%85%EC%9D%B4%EB%8A%94%E2%80%852%EC%9D%98%E2%80%85%EA%B1%B0%EB%93%AD%E2%80%85%EC%A0%9C%EA%B3%B1%EC%9D%84%E2%80%85%EC%A2%8B%EC%95%84%ED%95%B4%EF%BC%81%E2%80%85%EC%98%81%EC%9B%85%EC%9D%B4%EB%8A%94%E2%80%852%EC%9D%98%E2%80%85%EA%B1%B0%EB%93%AD%E2%80%85%EC%A0%9C%EA%B3%B1%EC%9D%84%E2%80%85%EC%A2%8B%EC%95%84%ED%95%B4%EF%BC%81/README.md) |
| Baekjoon | 20154 | 이 구역의 승자는 누구야？！ | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/20154.%E2%80%85%EC%9D%B4%E2%80%85%EA%B5%AC%EC%97%AD%EC%9D%98%E2%80%85%EC%8A%B9%EC%9E%90%EB%8A%94%E2%80%85%EB%88%84%EA%B5%AC%EC%95%BC%EF%BC%9F%EF%BC%81/README.md) |
| Baekjoon | 20218 | Figure Skating | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/20218.%E2%80%85Figure%E2%80%85Skating/README.md) |
| Baekjoon | 20438 | 출석체크 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/20438.%E2%80%85%EC%B6%9C%EC%84%9D%EC%B2%B4%ED%81%AC/README.md) |
| Baekjoon | 20492 | 세금 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/20492.%E2%80%85%EC%84%B8%EA%B8%88/README.md) |
| Baekjoon | 21313 | 문어 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/21313.%E2%80%85%EB%AC%B8%EC%96%B4/README.md) |
| Baekjoon | 21553 | 암호 만들기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/21553.%E2%80%85%EC%95%94%ED%98%B8%E2%80%85%EB%A7%8C%EB%93%A4%EA%B8%B0/README.md) |
| Baekjoon | 21758 | 꿀 따기 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/21758.%E2%80%85%EA%BF%80%E2%80%85%EB%94%B0%EA%B8%B0/README.md) |
| Baekjoon | 21866 | 추첨을 통해 커피를 받자 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/21866.%E2%80%85%EC%B6%94%EC%B2%A8%EC%9D%84%E2%80%85%ED%86%B5%ED%95%B4%E2%80%85%EC%BB%A4%ED%94%BC%EB%A5%BC%E2%80%85%EB%B0%9B%EC%9E%90/README.md) |
| Baekjoon | 21965 | 드높은 남산 위에 우뚝 선 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/21965.%E2%80%85%EB%93%9C%EB%86%92%EC%9D%80%E2%80%85%EB%82%A8%EC%82%B0%E2%80%85%EC%9C%84%EC%97%90%E2%80%85%EC%9A%B0%EB%9A%9D%E2%80%85%EC%84%A0/README.md) |
| Baekjoon | 22351 | 수학은 체육과목 입니다 3 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/22351.%E2%80%85%EC%88%98%ED%95%99%EC%9D%80%E2%80%85%EC%B2%B4%EC%9C%A1%EA%B3%BC%EB%AA%A9%E2%80%85%EC%9E%85%EB%8B%88%EB%8B%A4%E2%80%853/README.md) |
| Baekjoon | 22860 | 폴더 정리 （small） | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/22860.%E2%80%85%ED%8F%B4%EB%8D%94%E2%80%85%EC%A0%95%EB%A6%AC%E2%80%85%EF%BC%88small%EF%BC%89/README.md) |
| Baekjoon | 22970 | 문제 재탕 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/22970.%E2%80%85%EB%AC%B8%EC%A0%9C%E2%80%85%EC%9E%AC%ED%83%95/README.md) |
| Baekjoon | 23027 | 1번부터 문제의 상태가…？ | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/23027.%E2%80%851%EB%B2%88%EB%B6%80%ED%84%B0%E2%80%85%EB%AC%B8%EC%A0%9C%EC%9D%98%E2%80%85%EC%83%81%ED%83%9C%EA%B0%80%E2%80%A6%EF%BC%9F/README.md) |
| Baekjoon | 23056 | 참가자 명단 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/23056.%E2%80%85%EC%B0%B8%EA%B0%80%EC%9E%90%E2%80%85%EB%AA%85%EB%8B%A8/README.md) |
| Baekjoon | 23321 | 홍익 댄스파티 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/23321.%E2%80%85%ED%99%8D%EC%9D%B5%E2%80%85%EB%8C%84%EC%8A%A4%ED%8C%8C%ED%8B%B0/README.md) |
| Baekjoon | 23375 | Arm Coordination | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/23375.%E2%80%85Arm%E2%80%85Coordination/README.md) |
| Baekjoon | 23804 | 골뱅이 찍기 － ㄷ | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/23804.%E2%80%85%EA%B3%A8%EB%B1%85%EC%9D%B4%E2%80%85%EC%B0%8D%EA%B8%B0%E2%80%85%EF%BC%8D%E2%80%85%E3%84%B7/README.md) |
| Baekjoon | 23882 | 알고리즘 수업 － 선택 정렬 2 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/23882.%E2%80%85%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%E2%80%85%EC%88%98%EC%97%85%E2%80%85%EF%BC%8D%E2%80%85%EC%84%A0%ED%83%9D%E2%80%85%EC%A0%95%EB%A0%AC%E2%80%852/README.md) |
| Baekjoon | 24542 | 튜터－튜티 관계의 수 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/24542.%E2%80%85%ED%8A%9C%ED%84%B0%EF%BC%8D%ED%8A%9C%ED%8B%B0%E2%80%85%EA%B4%80%EA%B3%84%EC%9D%98%E2%80%85%EC%88%98/README.md) |
| Baekjoon | 24883 | 자동완성 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/24883.%E2%80%85%EC%9E%90%EB%8F%99%EC%99%84%EC%84%B1/README.md) |
| Baekjoon | 25083 | 새싹 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/25083.%E2%80%85%EC%83%88%EC%8B%B9/README.md) |
| Baekjoon | 25176 | 청정수열 （Easy） | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/25176.%E2%80%85%EC%B2%AD%EC%A0%95%EC%88%98%EC%97%B4%E2%80%85%EF%BC%88Easy%EF%BC%89/README.md) |
| Baekjoon | 25212 | 조각 케이크 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/25212.%E2%80%85%EC%A1%B0%EA%B0%81%E2%80%85%EC%BC%80%EC%9D%B4%ED%81%AC/README.md) |
| Baekjoon | 25304 | 영수증 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/25304.%E2%80%85%EC%98%81%EC%88%98%EC%A6%9D/README.md) |
| Baekjoon | 25323 | 수 정렬하기， 근데 이제 제곱수를 곁들인 | Platinum | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Platinum/25323.%E2%80%85%EC%88%98%E2%80%85%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0%EF%BC%8C%E2%80%85%EA%B7%BC%EB%8D%B0%E2%80%85%EC%9D%B4%EC%A0%9C%E2%80%85%EC%A0%9C%EA%B3%B1%EC%88%98%EB%A5%BC%E2%80%85%EA%B3%81%EB%93%A4%EC%9D%B8/README.md) |
| Baekjoon | 25373 | 벼락치기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/25373.%E2%80%85%EB%B2%BC%EB%9D%BD%EC%B9%98%EA%B8%B0/README.md) |
| Baekjoon | 25494 | 단순한 문제 （Small） | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/25494.%E2%80%85%EB%8B%A8%EC%88%9C%ED%95%9C%E2%80%85%EB%AC%B8%EC%A0%9C%E2%80%85%EF%BC%88Small%EF%BC%89/README.md) |
| Baekjoon | 25495 | 에어팟 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/25495.%E2%80%85%EC%97%90%EC%96%B4%ED%8C%9F/README.md) |
| Baekjoon | 25501 | 재귀의 귀재 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/25501.%E2%80%85%EC%9E%AC%EA%B7%80%EC%9D%98%E2%80%85%EA%B7%80%EC%9E%AC/README.md) |
| Baekjoon | 25594 | HG 음성기호 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/25594.%E2%80%85HG%E2%80%85%EC%9D%8C%EC%84%B1%EA%B8%B0%ED%98%B8/README.md) |
| Baekjoon | 25629 | 홀짝 수열 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/25629.%E2%80%85%ED%99%80%EC%A7%9D%E2%80%85%EC%88%98%EC%97%B4/README.md) |
| Baekjoon | 26083 | 유통기한 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/26083.%E2%80%85%EC%9C%A0%ED%86%B5%EA%B8%B0%ED%95%9C/README.md) |
| Baekjoon | 26150 | Identify， Sort， Index， Solve | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/26150.%E2%80%85Identify%EF%BC%8C%E2%80%85Sort%EF%BC%8C%E2%80%85Index%EF%BC%8C%E2%80%85Solve/README.md) |
| Baekjoon | 26516 | Mutint | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/26516.%E2%80%85Mutint/README.md) |
| Baekjoon | 26518 | 수열의 극한값 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/26518.%E2%80%85%EC%88%98%EC%97%B4%EC%9D%98%E2%80%85%EA%B7%B9%ED%95%9C%EA%B0%92/README.md) |
| Baekjoon | 26544 | Histogram Fencing | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/26544.%E2%80%85Histogram%E2%80%85Fencing/README.md) |
| Baekjoon | 26597 | 이 사람 왜 이렇게 1122를 좋아함？ | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/26597.%E2%80%85%EC%9D%B4%E2%80%85%EC%82%AC%EB%9E%8C%E2%80%85%EC%99%9C%E2%80%85%EC%9D%B4%EB%A0%87%EA%B2%8C%E2%80%851122%EB%A5%BC%E2%80%85%EC%A2%8B%EC%95%84%ED%95%A8%EF%BC%9F/README.md) |
| Baekjoon | 27106 | Making Change | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/27106.%E2%80%85Making%E2%80%85Change/README.md) |
| Baekjoon | 27466 | 그래서 대회 이름 뭐로 하죠 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/27466.%E2%80%85%EA%B7%B8%EB%9E%98%EC%84%9C%E2%80%85%EB%8C%80%ED%9A%8C%E2%80%85%EC%9D%B4%EB%A6%84%E2%80%85%EB%AD%90%EB%A1%9C%E2%80%85%ED%95%98%EC%A3%A0/README.md) |
| Baekjoon | 27512 | 스네이크 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/27512.%E2%80%85%EC%8A%A4%EB%84%A4%EC%9D%B4%ED%81%AC/README.md) |
| Baekjoon | 27621 | Sum of Three Cubes | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/27621.%E2%80%85Sum%E2%80%85of%E2%80%85Three%E2%80%85Cubes/README.md) |
| Baekjoon | 27866 | 문자와 문자열 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/27866.%E2%80%85%EB%AC%B8%EC%9E%90%EC%99%80%E2%80%85%EB%AC%B8%EC%9E%90%EC%97%B4/README.md) |
| Baekjoon | 27884 | 가희와 서울 지하철 3호선 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/27884.%E2%80%85%EA%B0%80%ED%9D%AC%EC%99%80%E2%80%85%EC%84%9C%EC%9A%B8%E2%80%85%EC%A7%80%ED%95%98%EC%B2%A0%E2%80%853%ED%98%B8%EC%84%A0/README.md) |
| Baekjoon | 27930 | 당신은 운명을 믿나요？ | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/27930.%E2%80%85%EB%8B%B9%EC%8B%A0%EC%9D%80%E2%80%85%EC%9A%B4%EB%AA%85%EC%9D%84%E2%80%85%EB%AF%BF%EB%82%98%EC%9A%94%EF%BC%9F/README.md) |
| Baekjoon | 27969 | I LOVE JavaScript | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/27969.%E2%80%85I%E2%80%85LOVE%E2%80%85JavaScript/README.md) |
| Baekjoon | 27971 | 강아지는 많을수록 좋다 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/27971.%E2%80%85%EA%B0%95%EC%95%84%EC%A7%80%EB%8A%94%E2%80%85%EB%A7%8E%EC%9D%84%EC%88%98%EB%A1%9D%E2%80%85%EC%A2%8B%EB%8B%A4/README.md) |
| Baekjoon | 27983 | 리본 （Easy） | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/27983.%E2%80%85%EB%A6%AC%EB%B3%B8%E2%80%85%EF%BC%88Easy%EF%BC%89/README.md) |
| Baekjoon | 28290 | 안밖？ 밖안？ 계단？ 역계단？ | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/28290.%E2%80%85%EC%95%88%EB%B0%96%EF%BC%9F%E2%80%85%EB%B0%96%EC%95%88%EF%BC%9F%E2%80%85%EA%B3%84%EB%8B%A8%EF%BC%9F%E2%80%85%EC%97%AD%EA%B3%84%EB%8B%A8%EF%BC%9F/README.md) |
| Baekjoon | 28419 | 더하기 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/28419.%E2%80%85%EB%8D%94%ED%95%98%EA%B8%B0/README.md) |
| Baekjoon | 28423 | 게임 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/28423.%E2%80%85%EA%B2%8C%EC%9E%84/README.md) |
| Baekjoon | 28702 | FizzBuzz | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/28702.%E2%80%85FizzBuzz/README.md) |
| Baekjoon | 29716 | 풀만한문제 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/29716.%E2%80%85%ED%92%80%EB%A7%8C%ED%95%9C%EB%AC%B8%EC%A0%9C/README.md) |
| Baekjoon | 30024 | 옥수수밭 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/30024.%E2%80%85%EC%98%A5%EC%88%98%EC%88%98%EB%B0%AD/README.md) |
| Baekjoon | 30218 | Weighted Window Sums | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/30218.%E2%80%85Weighted%E2%80%85Window%E2%80%85Sums/README.md) |
| Baekjoon | 30328 | Java Warriors | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/30328.%E2%80%85Java%E2%80%85Warriors/README.md) |
| Baekjoon | 30402 | 감마선을 맞은 컴퓨터 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/30402.%E2%80%85%EA%B0%90%EB%A7%88%EC%84%A0%EC%9D%84%E2%80%85%EB%A7%9E%EC%9D%80%E2%80%85%EC%BB%B4%ED%93%A8%ED%84%B0/README.md) |
| Baekjoon | 30456 | 바닥수 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/30456.%E2%80%85%EB%B0%94%EB%8B%A5%EC%88%98/README.md) |
| Baekjoon | 30469 | 호반우가 학교에 지각한 이유 2 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/30469.%E2%80%85%ED%98%B8%EB%B0%98%EC%9A%B0%EA%B0%80%E2%80%85%ED%95%99%EA%B5%90%EC%97%90%E2%80%85%EC%A7%80%EA%B0%81%ED%95%9C%E2%80%85%EC%9D%B4%EC%9C%A0%E2%80%852/README.md) |
| Baekjoon | 30794 | 가희와 클럽 오디션 1 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/30794.%E2%80%85%EA%B0%80%ED%9D%AC%EC%99%80%E2%80%85%ED%81%B4%EB%9F%BD%E2%80%85%EC%98%A4%EB%94%94%EC%85%98%E2%80%851/README.md) |
| Baekjoon | 30802 | 웰컴 키트 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/30802.%E2%80%85%EC%9B%B0%EC%BB%B4%E2%80%85%ED%82%A4%ED%8A%B8/README.md) |
| Baekjoon | 30821 | 별자리가 될 수 있다면 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/30821.%E2%80%85%EB%B3%84%EC%9E%90%EB%A6%AC%EA%B0%80%E2%80%85%EB%90%A0%E2%80%85%EC%88%98%E2%80%85%EC%9E%88%EB%8B%A4%EB%A9%B4/README.md) |
| Baekjoon | 30825 | 건공펀치 등차수열 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/30825.%E2%80%85%EA%B1%B4%EA%B3%B5%ED%8E%80%EC%B9%98%E2%80%85%EB%93%B1%EC%B0%A8%EC%88%98%EC%97%B4/README.md) |
| Baekjoon | 30970 | 선택의 기로 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/30970.%E2%80%85%EC%84%A0%ED%83%9D%EC%9D%98%E2%80%85%EA%B8%B0%EB%A1%9C/README.md) |
| Baekjoon | 30979 | 유치원생 파댕이 돌보기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/30979.%E2%80%85%EC%9C%A0%EC%B9%98%EC%9B%90%EC%83%9D%E2%80%85%ED%8C%8C%EB%8C%95%EC%9D%B4%E2%80%85%EB%8F%8C%EB%B3%B4%EA%B8%B0/README.md) |
| Baekjoon | 31395 | 정렬된 연속한 부분수열의 개수 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/31395.%E2%80%85%EC%A0%95%EB%A0%AC%EB%90%9C%E2%80%85%EC%97%B0%EC%86%8D%ED%95%9C%E2%80%85%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4%EC%9D%98%E2%80%85%EA%B0%9C%EC%88%98/README.md) |
| Baekjoon | 31428 | 엘리스 트랙 매칭 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/31428.%E2%80%85%EC%97%98%EB%A6%AC%EC%8A%A4%E2%80%85%ED%8A%B8%EB%9E%99%E2%80%85%EB%A7%A4%EC%B9%AD/README.md) |
| Baekjoon | 31460 | 초콜릿과 11과 팰린드롬 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/31460.%E2%80%85%EC%B4%88%EC%BD%9C%EB%A6%BF%EA%B3%BC%E2%80%8511%EA%B3%BC%E2%80%85%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC/README.md) |
| Baekjoon | 31495 | 그게 무슨 코드니．． | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/31495.%E2%80%85%EA%B7%B8%EA%B2%8C%E2%80%85%EB%AC%B4%EC%8A%A8%E2%80%85%EC%BD%94%EB%93%9C%EB%8B%88%EF%BC%8E%EF%BC%8E/README.md) |
| Baekjoon | 31562 | 전주 듣고 노래 맞히기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/31562.%E2%80%85%EC%A0%84%EC%A3%BC%E2%80%85%EB%93%A3%EA%B3%A0%E2%80%85%EB%85%B8%EB%9E%98%E2%80%85%EB%A7%9E%ED%9E%88%EA%B8%B0/README.md) |
| Baekjoon | 31738 | 매우 어려운 문제 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/31738.%E2%80%85%EB%A7%A4%EC%9A%B0%E2%80%85%EC%96%B4%EB%A0%A4%EC%9A%B4%E2%80%85%EB%AC%B8%EC%A0%9C/README.md) |
| Baekjoon | 31796 | 한빛미디어 （Easy） | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/31796.%E2%80%85%ED%95%9C%EB%B9%9B%EB%AF%B8%EB%94%94%EC%96%B4%E2%80%85%EF%BC%88Easy%EF%BC%89/README.md) |
| Baekjoon | 31797 | 아～파트 아파트 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/31797.%E2%80%85%EC%95%84%EF%BD%9E%ED%8C%8C%ED%8A%B8%E2%80%85%EC%95%84%ED%8C%8C%ED%8A%B8/README.md) |
| Baekjoon | 31963 | 두 배 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/31963.%E2%80%85%EB%91%90%E2%80%85%EB%B0%B0/README.md) |
| Baekjoon | 32154 | SUAPC 2024 Winter | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/32154.%E2%80%85SUAPC%E2%80%852024%E2%80%85Winter/README.md) |
| Baekjoon | 32209 | 다음 달에 봐요 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/32209.%E2%80%85%EB%8B%A4%EC%9D%8C%E2%80%85%EB%8B%AC%EC%97%90%E2%80%85%EB%B4%90%EC%9A%94/README.md) |
| Baekjoon | 32278 | 선택 가능성이 가장 높은 자료형 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/32278.%E2%80%85%EC%84%A0%ED%83%9D%E2%80%85%EA%B0%80%EB%8A%A5%EC%84%B1%EC%9D%B4%E2%80%85%EA%B0%80%EC%9E%A5%E2%80%85%EB%86%92%EC%9D%80%E2%80%85%EC%9E%90%EB%A3%8C%ED%98%95/README.md) |
| Baekjoon | 32282 | 너 그리고 나 （NAVILLERA） | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/32282.%E2%80%85%EB%84%88%E2%80%85%EA%B7%B8%EB%A6%AC%EA%B3%A0%E2%80%85%EB%82%98%E2%80%85%EF%BC%88NAVILLERA%EF%BC%89/README.md) |
| Baekjoon | 32283 | 진수 정렬 （Easy） | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/32283.%E2%80%85%EC%A7%84%EC%88%98%E2%80%85%EC%A0%95%EB%A0%AC%E2%80%85%EF%BC%88Easy%EF%BC%89/README.md) |
| Baekjoon | 32345 | 혼긱대학교 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/32345.%E2%80%85%ED%98%BC%EA%B8%B1%EB%8C%80%ED%95%99%EA%B5%90/README.md) |
| Baekjoon | 32357 | 더블팰린드롬 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/32357.%E2%80%85%EB%8D%94%EB%B8%94%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC/README.md) |
| Baekjoon | 32372 | 마법의 나침반 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/32372.%E2%80%85%EB%A7%88%EB%B2%95%EC%9D%98%E2%80%85%EB%82%98%EC%B9%A8%EB%B0%98/README.md) |
| Baekjoon | 32377 | 풍선 터트리기 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/32377.%E2%80%85%ED%92%8D%EC%84%A0%E2%80%85%ED%84%B0%ED%8A%B8%EB%A6%AC%EA%B8%B0/README.md) |
| Baekjoon | 32625 | 분할 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/32625.%E2%80%85%EB%B6%84%ED%95%A0/README.md) |
| Baekjoon | 32642 | 당구 좀 치자 제발 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/32642.%E2%80%85%EB%8B%B9%EA%B5%AC%E2%80%85%EC%A2%80%E2%80%85%EC%B9%98%EC%9E%90%E2%80%85%EC%A0%9C%EB%B0%9C/README.md) |
| Baekjoon | 32775 | 가희와 4시간의 벽 1 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/32775.%E2%80%85%EA%B0%80%ED%9D%AC%EC%99%80%E2%80%854%EC%8B%9C%EA%B0%84%EC%9D%98%E2%80%85%EB%B2%BD%E2%80%851/README.md) |
| Baekjoon | 32776 | 가희와 4시간의 벽 2 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/32776.%E2%80%85%EA%B0%80%ED%9D%AC%EC%99%80%E2%80%854%EC%8B%9C%EA%B0%84%EC%9D%98%E2%80%85%EB%B2%BD%E2%80%852/README.md) |
| Baekjoon | 32777 | 가희와 서울 지하철 2호선 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/32777.%E2%80%85%EA%B0%80%ED%9D%AC%EC%99%80%E2%80%85%EC%84%9C%EC%9A%B8%E2%80%85%EC%A7%80%ED%95%98%EC%B2%A0%E2%80%852%ED%98%B8%EC%84%A0/README.md) |
| Baekjoon | 32778 | 가희와 부역명 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/32778.%E2%80%85%EA%B0%80%ED%9D%AC%EC%99%80%E2%80%85%EB%B6%80%EC%97%AD%EB%AA%85/README.md) |
| Baekjoon | 32779 | 가희와 전기 요금 1 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/32779.%E2%80%85%EA%B0%80%ED%9D%AC%EC%99%80%E2%80%85%EC%A0%84%EA%B8%B0%E2%80%85%EC%9A%94%EA%B8%88%E2%80%851/README.md) |
| Baekjoon | 32929 | UOS 문자열 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/32929.%E2%80%85UOS%E2%80%85%EB%AC%B8%EC%9E%90%EC%97%B4/README.md) |
| Baekjoon | 32943 | 자리 신청 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/32943.%E2%80%85%EC%9E%90%EB%A6%AC%E2%80%85%EC%8B%A0%EC%B2%AD/README.md) |
| Baekjoon | 32951 | AI 선도대학 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/32951.%E2%80%85AI%E2%80%85%EC%84%A0%EB%8F%84%EB%8C%80%ED%95%99/README.md) |
| Baekjoon | 33042 | 이변마작 1 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/33042.%E2%80%85%EC%9D%B4%EB%B3%80%EB%A7%88%EC%9E%91%E2%80%851/README.md) |
| Baekjoon | 33541 | 2025는 무엇이 특별할까？ | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/33541.%E2%80%852025%EB%8A%94%E2%80%85%EB%AC%B4%EC%97%87%EC%9D%B4%E2%80%85%ED%8A%B9%EB%B3%84%ED%95%A0%EA%B9%8C%EF%BC%9F/README.md) |
| Baekjoon | 33542 | 극적인 승리 | Gold | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Gold/33542.%E2%80%85%EA%B7%B9%EC%A0%81%EC%9D%B8%E2%80%85%EC%8A%B9%EB%A6%AC/README.md) |
| Baekjoon | 33631 | 1교시： 가정 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/33631.%E2%80%851%EA%B5%90%EC%8B%9C%EF%BC%9A%E2%80%85%EA%B0%80%EC%A0%95/README.md) |
| Baekjoon | 33632 | 2교시： 체육 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/33632.%E2%80%852%EA%B5%90%EC%8B%9C%EF%BC%9A%E2%80%85%EC%B2%B4%EC%9C%A1/README.md) |
| Baekjoon | 33845 | PNUPC에 한 번도 빠지지 않고 출연한 산지니가 새삼 대단하다고 느껴지네 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/33845.%E2%80%85PNUPC%EC%97%90%E2%80%85%ED%95%9C%E2%80%85%EB%B2%88%EB%8F%84%E2%80%85%EB%B9%A0%EC%A7%80%EC%A7%80%E2%80%85%EC%95%8A%EA%B3%A0%E2%80%85%EC%B6%9C%EC%97%B0%ED%95%9C%E2%80%85%EC%82%B0%EC%A7%80%EB%8B%88%EA%B0%80%E2%80%85%EC%83%88%EC%82%BC%E2%80%85%EB%8C%80%EB%8B%A8%ED%95%98%EB%8B%A4%EA%B3%A0%E2%80%85%EB%8A%90%EA%BB%B4%EC%A7%80%EB%84%A4/README.md) |
| Baekjoon | 33846 | 삽입 정렬을 해볼까 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/33846.%E2%80%85%EC%82%BD%EC%9E%85%E2%80%85%EC%A0%95%EB%A0%AC%EC%9D%84%E2%80%85%ED%95%B4%EB%B3%BC%EA%B9%8C/README.md) |
| Baekjoon | 33847 | 태종대 낚시 맛집 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/33847.%E2%80%85%ED%83%9C%EC%A2%85%EB%8C%80%E2%80%85%EB%82%9A%EC%8B%9C%E2%80%85%EB%A7%9B%EC%A7%91/README.md) |
| Baekjoon | 33923 | 인경호 울타리 공사 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/33923.%E2%80%85%EC%9D%B8%EA%B2%BD%ED%98%B8%E2%80%85%EC%9A%B8%ED%83%80%EB%A6%AC%E2%80%85%EA%B3%B5%EC%82%AC/README.md) |
| Baekjoon | 33924 | 신묘마루의 요술망치 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/33924.%E2%80%85%EC%8B%A0%EB%AC%98%EB%A7%88%EB%A3%A8%EC%9D%98%E2%80%85%EC%9A%94%EC%88%A0%EB%A7%9D%EC%B9%98/README.md) |
| Baekjoon | 33925 | 쿠키런 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/33925.%E2%80%85%EC%BF%A0%ED%82%A4%EB%9F%B0/README.md) |
| Baekjoon | 34073 | DORO | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/34073.%E2%80%85DORO/README.md) |
| Baekjoon | 34099 | 뭔가 이미 있을 것 같은 순열 문제 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/34099.%E2%80%85%EB%AD%94%EA%B0%80%E2%80%85%EC%9D%B4%EB%AF%B8%E2%80%85%EC%9E%88%EC%9D%84%E2%80%85%EA%B2%83%E2%80%85%EA%B0%99%EC%9D%80%E2%80%85%EC%88%9C%EC%97%B4%E2%80%85%EB%AC%B8%EC%A0%9C/README.md) |
| Baekjoon | 34225 | 현대모비스 부품 조립 | Silver | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Silver/34225.%E2%80%85%ED%98%84%EB%8C%80%EB%AA%A8%EB%B9%84%EC%8A%A4%E2%80%85%EB%B6%80%ED%92%88%E2%80%85%EC%A1%B0%EB%A6%BD/README.md) |
| Baekjoon | 34236 | 숭고한에 어서오세요 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/34236.%E2%80%85%EC%88%AD%EA%B3%A0%ED%95%9C%EC%97%90%E2%80%85%EC%96%B4%EC%84%9C%EC%98%A4%EC%84%B8%EC%9A%94/README.md) |
| Baekjoon | 34552 | 디딤돌 장학금 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/34552.%E2%80%85%EB%94%94%EB%94%A4%EB%8F%8C%E2%80%85%EC%9E%A5%ED%95%99%EA%B8%88/README.md) |
| Baekjoon | 34553 | 알파벳 점수 계산기 | Bronze | [풀이 보기](./problems/%EB%B0%B1%EC%A4%80/Bronze/34553.%E2%80%85%EC%95%8C%ED%8C%8C%EB%B2%B3%E2%80%85%EC%A0%90%EC%88%98%E2%80%85%EA%B3%84%EC%82%B0%EA%B8%B0/README.md) |
| AtCoder | abc456 | A_Dice | - | [풀이 보기](./problems/atcoder/abc456/A_Dice.md) |
| AtCoder | abc456 | B_456 | - | [풀이 보기](./problems/atcoder/abc456/B_456.md) |
| AtCoder | abc457 | B_Arrays | - | [풀이 보기](./problems/atcoder/abc457/B_Arrays.md) |
| AtCoder | abc452 | B_Draw_Frame | - | [풀이 보기](./problems/atcoder/abc452/B_Draw_Frame.md) |
| AtCoder | abc454 | B_Mapping | - | [풀이 보기](./problems/atcoder/abc454/B_Mapping.md) |
| AtCoder | abc453 | B_Sensor_Data_Logging | - | [풀이 보기](./problems/atcoder/abc453/B_Sensor_Data_Logging.md) |
| AtCoder | abc455 | B_Spiral_Galaxy | - | [풀이 보기](./problems/atcoder/abc455/B_Spiral_Galaxy.md) |
| AtCoder | abc452 | C_Fishbones | - | [풀이 보기](./problems/atcoder/abc452/C_Fishbones.md) |
| AtCoder | abc457 | C_Long_Sequence | - | [풀이 보기](./problems/atcoder/abc457/C_Long_Sequence.md) |
| AtCoder | abc456 | C_Not_Adjacent | - | [풀이 보기](./problems/atcoder/abc456/C_Not_Adjacent.md) |
| AtCoder | abc453 | C_Sneaking_Glances | - | [풀이 보기](./problems/atcoder/abc453/C_Sneaking_Glances.md) |
| AtCoder | abc454 | C_Straw_Millionaire | - | [풀이 보기](./problems/atcoder/abc454/C_Straw_Millionaire.md) |
| AtCoder | abc455 | C_Vanish | - | [풀이 보기](./problems/atcoder/abc455/C_Vanish.md) |
| AtCoder | abc454 | D_(xx) | - | [풀이 보기](./problems/atcoder/abc454/D_%28xx%29.md) |
| AtCoder | abc455 | D_Card_Pile_Query | - | [풀이 보기](./problems/atcoder/abc455/D_Card_Pile_Query.md) |

</details>
<!-- problems:end -->

---

## 📂 디렉토리 구조 (Directory Structure)

```text
algorithm-archive/
├── problems/             # 지금 풀고 있는 것
│   ├── 백준/             # BOJ 풀이 (난이도별 분류)
│   ├── atcoder/          # AtCoder 콘테스트 풀이
│   └── sw_expert_academy/
├── archive/              # Quartz 블로그 시절 원고. 더 안 건드린다
│   ├── dacon/            # 대회 회고 원본 → 지금은 블로그에 있다
│   └── kaggle/
└── scripts/              # 템플릿 포맷팅 및 통계 갱신 Python 스크립트
```
