n = int(input())
word = []
alpha = []

# 단어 입력 받기
for _ in range(n):
    word.append(input())
cnt = 0

# # 풀이1 : 반복문
# # 단어입력 함수
# def count(word):
#     for idx in range(len(word)-1):
#         if word[idx] != word[idx+1]:
#             # 이미 나온 단어면 false
#             if word[idx] in alpha:
#                 return False
#             else:
#                 alpha.append(word[idx])
#
#     # 마지막 단어는 따로 체크해주어야 함. 반복문에서는 len(word)-1 까지만 비교
#     if word[-1] in alpha:
#         return False
#     return True
#
# for w in word:
#     word = []
#     alpha = []
#     cnt += 1 if count(w) == True else 0
# print(cnt)

def towPointer(word):
    left, right = 0,0
    while right < len(word):
        if word[left] == word[right]:
            right +=1
        else:
            if word[right] in alpha:
                return False
            else:
                alpha.append(word[left])
                left = right
    return True

# 플이2: 투 포인터
cnt = 0
for w in word:
    word = []
    alpha = []
    cnt += 1 if towPointer(w) == True else 0

print(cnt)

# #제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
# 77960061	mlac	 1316	맞았습니다!!	31252	44	Python 3 / 수정	566	30초 전 -> 반복문
# 77935599	mlac	 1316	맞았습니다!!	31120	44	Python 3 / 수정	500	-> 투포인터

# 투포인터 사용해도 시간/공간 크게 줄어들지 않음