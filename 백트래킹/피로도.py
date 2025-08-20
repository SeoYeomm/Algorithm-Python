# 프로그래머스 완전탐색 백트래킹으로 풀기 
# 백트래킹 (dfs)

def solution(k, dungeons):
    answer = 0 
    n = len (dungeons)
    visited = [False] * n
    
    def dfs(k,cnt):
        nonlocal answer
        answer = max(answer, cnt)
        
        for i in range(n):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                dfs(k-dungeons[i][1], cnt+1)
                visited[i] = False
    dfs(k,0)
    return answer