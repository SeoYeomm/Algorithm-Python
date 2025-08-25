# 백준 11724
import sys 
input = sys.stdin.readline # 시간 초과 방지 

n, m = map(int,input().split()) # 정점, 간선 
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1) 

for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v) # 무방향 그래프랑 둘다 넣음 
    graph[v].append(u)
    
def dfs (start):
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if not visited[node]:
            visited[node] = True
            
            for idj in graph[node]: # 해당 정점과 연결된 정점들 확인 
                if not visited[idj]:
                    stack.append(idj)
    
cnt = 0 
for i in range(1, n+1):
    if not visited[i]: # 1,2,5/ 3,4,6 -> 2개
        dfs(i) 
        cnt += 1
        
print(cnt)
                