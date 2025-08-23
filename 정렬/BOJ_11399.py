N = int(input())
s = 0 
people = list(map(int, input().split()))
    
people.sort()

for i in range(N+1):
    s += sum(people[:i])
print(s)
    