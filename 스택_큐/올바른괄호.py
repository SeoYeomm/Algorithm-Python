def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif stack: # 비어있지 않으면 
            stack.pop()
        else: # ) 이면서 비어있으면 
            return False 
    if not stack: # 비어있으면 
        return True
    else:
        return False