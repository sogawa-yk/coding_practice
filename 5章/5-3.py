N = int(input())
P = list(map(int, input().split()))

dp = [[False for _ in range(100**2)] for _ in range(N+1)]
dp[0][0] = True
for i in range(1, N+1):
    for j in range(100**2):
        # i問目を解く場合
        if j - P[i-1] >= 0:
            if dp[i-1][j-P[i-1]]: dp[i][j] = True
        # i問目を解かない場合
        if dp[i-1][j]: dp[i][j] = True
 
cnt = 0       
for j in range(100**2):
    if dp[N][j]: cnt += 1
    
print(cnt)