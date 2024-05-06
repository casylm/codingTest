n = int(input())
word = []
alpha = []
def count(word):
    for idx in range(len(word)-1):
        if word[idx] != word[idx+1]:
            if word[idx] in alpha:
                return False
            else:
                alpha.append(word[idx])
    if word[-1] in alpha:
        return False
    return True

for _ in range(n):
    word.append(input())
cnt = 0

for w in word:
    word = []
    alpha = []
    cnt += 1 if count(w) == True else 0
print(cnt)

# 투 포인터로도 풀수 있을듯