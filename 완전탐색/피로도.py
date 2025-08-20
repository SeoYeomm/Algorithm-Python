# 현재 피로도 k, [던전별 최소 필요 피로도, 소모 피로도]
# 유저가 탐험 가능한 최대 던전 수 
# 순열로 모든 경우 (순서가 중요)

from itertools import permutations

def solution(k, dungeons):
    answer = []
    result = list(permutations(dungeons,len(dungeons)))
    
    for res in result:
        cur_k = k # 매 순열 조합마다 k 초기화 
        cnt = 0 
        
        for r in res:
            if cur_k >= r[0]:
                cur_k -= r[1]
                cnt += 1

        answer.append(cnt)
    return max(answer)