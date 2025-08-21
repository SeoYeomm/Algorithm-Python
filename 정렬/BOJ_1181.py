# 백준 1181 단어 정렬 
# 길이가 짧은 것 -> 같으면 사전 순으로 & 중복 제거 

n = int(input())
word = []

for i in range(n):
    w = input()
    word.append(w)
    
word = list(set(word)) # 중복 제거   
word.sort(key = lambda x: (len(x),x)) 
# len(x)로 먼저 정렬 후 
# 길이가 같으면 사전 순으로

for w in word:
    print(w)