# 각 원소는 1000이하니까 3번 곱함
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers)) # numbers의 원소들 모두 문자열로 변경 
    numbers.sort (key = lambda x: x*3, reverse = True) # 문자열 정렬하면 사전순으로 정렬 1 < 10 < 12 < 2 < 21
    # 사전순 정렬 앞자리부터 비교
    
    answer = ''.join(numbers) 
    # 모두 0인 경우 예외 처리 
    return answer if answer[0]!= '0' else '0'
