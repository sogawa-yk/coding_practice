    """DPの表を完成させて、逆をたどる

    Returns:
        [type]: [description]
    """

s = input()
t = input()

def chmax(a, b):
    if a>b:
        return a
    else:
        return b

dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)] # sをi文字目、tをj文字目まで見たときの最長共通部分列の長さ

for i in range(1, len(s)+1):
    for j in range(1, len(t)+1):
        if s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + 1 # sのi文字目とtのj文字目が同じ場合、その文字は採用
        else: dp[i][j] = chmax(dp[i-1][j], dp[i][j-1]) #sのi文字目とtのj文字目が違う場合、どちらかの文字は採用されないので、最長共通部分列が長い方を採用

print(dp[len(s)][len(t)])