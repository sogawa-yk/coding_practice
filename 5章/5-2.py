
N, W = map(int, input().split())
A = list(map(int, input().split()))


# def func(n, w):
#     if w == 0:
#         return True
#     if n == 0:
#         return False
#     if A[n-1] > w:
#         return False
    
#     return func(n-1, w-A[n-1]) | func(n-1, w)

# print(func(N, W))



# dp[i][j] を、最初のi個の整数の中からいくつか選んだ総和がjにできるかどうかを表すブール値とする
dp = [[False for _ in range(W+1)] for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    for j in range(W+1):
            # A[i]を選ばない場合
            if dp[i][j]: dp[i+1][j] = True
            
            # A[i]を選ぶ場合
            if A[i] <= j and dp[i][j-A[i]]: dp[i+1][j] = True
            
print(dp[N][W])