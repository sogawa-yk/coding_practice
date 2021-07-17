N, W, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [[False for _ in range(W+1)] for _ in range(N+1)]

dp[0][0] = True # dp[n][w]は、n-1個目までの整数からwを作れるかどうかを表すブール値

for n in range(1, N+1):
    for w in range(W+1):
        # A[n-1]を入れる場合
        if w > A[n-1]:
            if dp[n-1][w-A[n-1]]: dp[n][w] = True
        # A[n-1]を入れない場合
        if dp[n-1][w]: dp[n][w] = True
        
cnt = 0
for k in range(K):
    if dp[k][W]: cnt += 1
    
print(cnt)