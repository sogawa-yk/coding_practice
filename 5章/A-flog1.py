import sys
sys.setrecursionlimit(10**6)

N = int(input())
h = list(map(int, input().split()))
dp = [-1 for _ in range(N)]

# for i in range(N):
#     if i == 0:
#         dp[i] = 0
#     elif i == 1:
#         dp[i] = abs(h[1] - h[0])
#     else:
#         tmp1 =  abs(h[i] - h[i-1])
#         tmp2 = abs(h[i] - h[i-2])
#         if tmp1+dp[i-1] < tmp2+dp[i-2]:
#             dp[i] = tmp1 + dp[i-1]
#         else:
#             dp[i] = tmp2 + dp[i-2]


def func(i):
    if i == 0:
        dp[i] = 0
        return 0
    elif i == 1:
        dp[i] = abs(h[0] - h[1])
        return abs(h[0] - h[1])
    
    if dp[i-1] == -1:
        tmp1 = func(i-1) + abs(h[i] - h[i-1])
    else:
        tmp1 = dp[i-1] + abs(h[i] - h[i-1])
    if dp[i-2] == -1:
        tmp2 = func(i-2) + abs(h[i] - h[i-2])
    else:
        tmp2 = dp[i-2] + abs(h[i]-h[i-2])
        
    if tmp1 < tmp2:
        dp[i] = tmp1
        return tmp1
    else:
        dp[i] = tmp2
        return tmp2


print(func(N-1))