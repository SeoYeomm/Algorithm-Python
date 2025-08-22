# 큐: 방문좌표 표시
from collections import deque

def solution(maps):
    answer = 0
    n = len(maps) # 세로
    m = len(maps[0]) # 가로
    queue = deque()
    queue.append((0,0))
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while queue:
        y,x = queue.popleft()
        for i in range (4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<=ny<n and 0<=nx<m and maps[ny][nx] ==1:
                maps[ny][nx] = maps[y][x] + 1 
                queue.append((ny,nx))
    answer = maps[n-1][m-1]
    if answer == 1:
        return -1
    else:
        return answer
    
    return answer