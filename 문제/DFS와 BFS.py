import sys
from collections import deque

v,l,start = map(int,input().split())
mlist = [[] for _ in range(v+1)]
stack = []
visited = [False] * (v+1)
visited2 = [False] * (v+1)
mlist[0].append(0)
result = []
queue = deque([])

for _ in range(l):
    s,f = map(int,input().split())
    mlist[s].append(f)
    mlist[f].append(s)

# 오름차순 정렬
for idx,l in enumerate(mlist):
    mlist[idx] = sorted(l)

def dfs(v,visited):
    visited[v] = True
    result.append(v)
    for i in mlist[v]:
        if visited[i] == False:
            dfs(i,visited)
def bfs(v,queue):

    while queue:
        q = queue.popleft()
        for s in mlist[q]:
            if visited2[s] == False:
                visited2[s] = True
                queue.append(s)
                result.append(s)
dfs(start,visited)

print(' '.join(map(str,result)))

result = []
queue.append(start)
visited2[start] = True
result.append(start)
bfs(start,queue)
print(' '.join(map(str,result)))