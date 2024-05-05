n = int(input())

# 거스름돈
result = 1000 - n
# 거스름돈 종류
l = [500,100,50,10,5,1]
cnt = 0

for x in l:
    while result >= x:
        result -= x
        cnt +=1

print(cnt)