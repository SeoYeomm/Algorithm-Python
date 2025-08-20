# 백준 1012 유기농 배추
# BFS 큐

from collections import deque 

# 상하좌우 이동 
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input()) # 테스트케이스 수 

for i in range (T): 
    cnt = 0
    m, n, k = map(int,input().split()) # 가로, 세로, 1의 개수 
    graph = [[0]*m for i in range (n)]
    visited = [[False]*m for i in range(n)]
    queue = deque()
    
    # 그래프에 1 추가하기 
    for i in range(k):
        x, y = map(int,input().split())
        graph[y][x] = 1 
        
    # 1인 모인 곳 찾기 
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1 and not visited[y][x]:
                
                cnt += 1 
                queue.append((y,x)) 
                visited[y][x] = True
                
                while queue:
                    cy,cx = queue.popleft() 
                
                    # 1인 곳에서 상하좌우 이동하기  
                    for i in range(4):
                        nx = cx + dx[i]
                        ny = cy + dy[i]
                        
                        # 이동한 좌표가 그래프 내부 && 방문x -> 큐에 넣기 
                        if 0<=nx <m and 0<=ny<n:
                            if not visited[ny][nx] and graph[ny][nx] == 1:
                                visited[ny][nx] = True
                                queue.append((ny,nx))

    print(cnt) 

