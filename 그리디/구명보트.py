# 구명보트 최소 개수 return 
# 투포인터 (가장 가벼운 사람과 가장 무거운 사람을 합)

def solution(people, limit):
    answer = 0
    people.sort() 
    
    start = 0
    end = len (people) - 1
    
    while start <= end:
        if people[start] + people[end] <=limit:
            start += 1
            end -= 1
        else:
            end -= 1 
        answer += 1
        
    return answer
        
                
                
        