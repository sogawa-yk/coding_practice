N = int(input())
A, B, C = [], [], []
for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

    
def chmax(a, b):
    if a > b:
        return a
    else:
        return b
    
dp = [[-1, -1, -1] for _ in range(N)] # N*3 のリスト　どの活動をしたかによる　dp[i][1]は,i日目にBを行ったときの最大価値が入る

for i in range(N):
    if i==0:
        dp[i][0] = A[0]
        dp[i][1] = B[0]
        dp[i][2] = C[0]
    else:
        dp[i][0] = chmax(dp[i-1][1], dp[i-1][2]) + A[i]
        dp[i][1] = chmax(dp[i-1][0], dp[i-1][2]) + B[i]
        dp[i][2] = chmax(dp[i-1][0], dp[i-1][1]) + C[i]
        
print(max(dp[-1]))