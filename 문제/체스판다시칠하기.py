n, m = map(int,input().split())
chess = []

def count(sx,sy,result,chess,start):
    cnt = 0
    i,j = sx,sy # 3,6

    for j in range(sy,sy+8): # 14
        for i in range(sx,sx+8): # 11
            if chess[j][i] != start:
                cnt +=1
            start = 'W' if (start == 'B') else 'B'
        start = 'W' if (start == 'B') else 'B'
    return cnt

for _ in range(n):
    chess.append(list(input()))

w = len(chess[0])-8+1
h = len(chess)-8+1
result = 100000

for sx in range(w):
    for sy in range(h):
        result = min(count(sx,sy,result,chess,'B'),count(sx,sy,result,chess,'W'),result)

print(result)

# 제출 번호	아이디	문제	    결과	        메모리	시간	언어	        코드 길이
# 77890401	mlac	 1018	맞았습니다!!	111520	148	PyPy3 / 수정	1283