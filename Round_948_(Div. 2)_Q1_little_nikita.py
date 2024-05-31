t = int(input())  

for _ in range(t):
    n, m = map(int, input().split()) 
    
    if n < m or (n - m) % 2 != 0:
        print("No")
    else:
        print("Yes")
