# 가능한 모든 경우 넣어놓고 word가 인자로 들어오면 해당 index 반환

def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    def dfs (cnt, w):
        if cnt == 5:
            return 
        else:
            for i in range(5):
                words.append(w+vowels[i])
                dfs(cnt+1, w + vowels[i])
            
    dfs(0, '')
    return words.index(word) + 1