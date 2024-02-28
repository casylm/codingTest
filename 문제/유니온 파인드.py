def solution(nums):
    answer = 0
    li = []
    l = len(nums)//2

    for x in nums:
        if answer >= l:
            break
        if x in li:
            continue
        li.append(x)
        answer +=1
    return answer