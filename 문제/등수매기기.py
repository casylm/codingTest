# # 입력1
# n = int(input())
# score = []
# visited = [False] * (n+1)
#
# for _ in range(n):
#     score.append(int(input()))

# 입력2
import sys
n = int(sys.stdin.readline())
score = []

for _ in range(n):
    score.append(int(sys.stdin.readline()))
score.sort()#
answer = 0

# for idx,s in enumerate(score):
#     answer += abs((idx+1)-s)

for idx in range(1,n+1):
    answer += abs(idx-score[idx-1])
print(answer)

# 궁금한 것
# 제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
# 77904226	mlac	 2012	맞았습니다!!	52504	492	Python 3 / 수정	513	21초 전
# 77904201	mlac	 2012	맞았습니다!!	140696	312	PyPy3 / 수정	210
# pypy 로 돌렸을때보다 python으로 돌릴때 메모리 1/3 수준임. 왜?