memo = [-1 for _ in range(10000)]

def tri(n):
    
    if n==0:
        return 0
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        if memo[n-1] == -1:
            memo[n-1] = tri(n-1)
        if memo[n-2] == -1:
            memo[n-2] = tri(n-2)
        if memo[n-3] == -1:
            memo[n-3] = tri(n-3)
        
        return memo[n-1] + memo[n-2] + memo[n-3]
    
print(tri(int(input())))