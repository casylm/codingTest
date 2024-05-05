def solution(tickets):
    answer = []
    visited = [False] * len(tickets)

    # def find(d,a):
    #     answer.append(a)
    #     if sum(l) == 0:
    #         result.append(answer)
    #         anwer = []
    #         return
    #     for idx, t in enumerate(tickets):
    #         if l[idx] == 0:
    #             continue
    #         if a == t[0]:
    #             l[idx] = 0
    #             find(t[0],t[1])
    #             l[idx] = 1
    # 탐색
    def dfs(now, path):
        # 종료조건
        if len(path) == len(tickets) + 1:
            # 마지막은 도착지까지 import 하므로
            answer.append(path)
            return

        for idx, t in enumerate(tickets):
            if now == t[0] and visited[idx] == False:
                visited[idx] = True
                dfs(t[1], path + [t[1]])
                visited[idx] = False

    dfs("ICN", ["ICN"])

    # 정렬 1) 처음에 하고(lambda) 탐색? or 마지막에 정렬?
    # 놓친 것 : 항상 icn 공항에서 출발한다 -> 이걸 알았다면 dfs 함수 1개로 만들 수 있었지만, 생각을 하지 않아 출발지를 전체로 공항으로 생각하여 for문을 한개 더 만듦
    answer.sort()
    return answer[0]

# 참고
# https://lottegiantsv3.tistory.com/27#google_vignette