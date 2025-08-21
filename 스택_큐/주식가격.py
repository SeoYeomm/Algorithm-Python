# [3,1] 이면 [1,0] 나와야 함 
from collections import deque

def solution(prices):
    answer = []
    t = 0
    price = deque(prices)
    
    while price:
        p = price.popleft()
        t = 0
        for i in price:
            t += 1
            if p > i: # 하락
                break
            # 원래코드대로 하면 바로 뒤에 하락해도 반영 안됨 
            # if p <= i:
            #     t += 1
        answer.append(t)
    return answer
        