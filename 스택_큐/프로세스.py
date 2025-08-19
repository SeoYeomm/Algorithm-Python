from collections import deque

def solution(priorities, location):
    cnt = 0
    queue = deque(enumerate(priorities))
    
    while len(queue)>0: 
        p = queue.popleft()
        
        if queue and p[1] < max(q[1] for q in queue):  
            # queue가 비어있으면 max 부를 때 오류 생김
            # 예외처리 해줘야 함 
            queue.append(p)
            
        else:
            cnt += 1
            if p[0] == location:
                return cnt