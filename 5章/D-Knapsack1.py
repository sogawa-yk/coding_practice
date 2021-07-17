def chmax(a, b):
    if a>b:
        return a
    else:
        return b


w_list, v_list = [], []
N, W = map(int, input().split())
for _ in range(N):
    w, v = map(int, input().split())
    w_list.append(w)
    v_list.append(v)
    
dp = [[0 for _ in range(W+1)] for _ in range(N+1)] # dp[i][j]は、i番目までの商品から重さjの場合の価値の最大値

for i in range(1, N+1):
    for j in range(1, W+1):
        # i番目の商品を入れる場合
        if w_list[i-1] <= j: # 入れれるか確認
            dp[i][j] = chmax(dp[i-1][j-w_list[i-1]]+v_list[i-1], dp[i-1][j])
        # 入れない場合
        dp[i][j] = chmax(dp[i-1][j], dp[i][j])
        
print(dp[N][W])