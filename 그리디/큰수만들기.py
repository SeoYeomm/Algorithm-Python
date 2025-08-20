# k개의 수 제거했을 때 얻을 수 있는 가장 큰 수 반환 
# combination 조합으로 풀면 시간초과 뜸 
# 스택으로 풀기

def solution(number, k):
    ans = [] # 가장 큰 수 반환  
    for n in number:
        while k > 0 and ans and ans[-1] < n: 
            ans.pop() # 앞의 숫자가 현재 숫자보다 작으면 pop 
            k -= 1 
        ans.append(n) # 현재 숫자는 무조건 넣음 
        
    if k > 0: # 뒤에서부터 남은 k만큼 제거
        ans = ans[:-k]
    return ''.join(ans)