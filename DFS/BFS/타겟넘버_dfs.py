# dfs 재귀 

def solution(numbers, target):
    def dfs(idx, s):   # 현재 인덱스, 지금까지 합
        # 1) 종료 조건: 모든 숫자 다 쓴 경우
        if idx == len(numbers):
            if s == target:
                return 1   # 경우의 수 하나 발견
            else:
                return 0

        # 2) 아직 남은 숫자가 있으면, +와 - 두 갈래 탐색
        return dfs(idx+1, s+numbers[idx]) + dfs(idx+1, s-numbers[idx])

    # 3) 처음엔 아무것도 안 쓴 상태에서 시작
    return dfs(0, 0)


