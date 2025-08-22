# 인용 횟수가 h번 이상인 논문이 적어도 h편 
# h 최대값

def solution(citations):
    citations.sort(reverse = True)
    h = 0
    for i, c in enumerate(citations, start = 1):
        if c >= i:
            h = i
        else:
            break
    return h
