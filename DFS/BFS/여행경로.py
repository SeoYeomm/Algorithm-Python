# dfs 재귀, 백트래킹

def solution(tickets):
    tickets.sort(key = lambda x: x[1]) # 도착지 기준으로 정렬 
    n = len(tickets)
    visited= [False] * n
    
    def dfs (now, path):
        if len(path) == n+1: 
            return path 
        
        for i, (start, end) in enumerate(tickets):
            if not visited[i] and start == now:
                visited[i] = True
                result = dfs(end, path+[end]) # 끝까지 가면 성공 
                visited[i] = False # 아니면 티켓 되돌려 놓기
                if result:  # None이 아니라면 경로 반환
                    return result
        return None
    
    return dfs("ICN", ["ICN"])