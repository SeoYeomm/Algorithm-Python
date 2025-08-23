def solution(clothes):
    answer = 1
    dict = {}
    
    for c, kind in clothes:
        dict[kind] = dict.get(kind,0)+1 # get은 딕셔너리에서 특정 키의 값 뽑을 때 사용
        
    for cnt in dict.values():
        answer *= (cnt+1) # (동그란 안경, 검정 선글라스, 안 쓰는 경우) -> +1 해줌 
        
    return answer -1 # 아무것도 안 입은 경우의 수 빼줌 