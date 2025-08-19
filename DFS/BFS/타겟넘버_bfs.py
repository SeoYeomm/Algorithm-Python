# BFS 큐
from collections import deque

def solution(numbers, target):
    cnt = 0
    q = deque()  # 큐에 (현재 합, 인덱스) 추가 
    q.append((0,0)) # 처음 상태 
    
    while q: 
        s, idx = q.popleft()
        
        if idx == len(numbers):
            if s == target:
                cnt += 1 
        else:
            q.append((s + numbers[idx], idx+1))
            q.append((s - numbers[idx], idx+1))
    
    return cnt