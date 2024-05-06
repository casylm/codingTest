import sys

n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = list(set(arr))
arr.sort()
left,right = 0,0
result = int(2e9)

while left <= right and right<n:
    temp = arr[right]-arr[left]
    temp = abs(temp)
    if temp < m:
        right +=1
    else:
        result = min(result,temp)
        left +=1
print(result)