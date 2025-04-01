T, M = map(int, input().split())
t, w = [], []
for i in range(M):
    ti, wi = map(int, input().split())
    t.append(ti)
    w.append(wi)

dp = [0] * (T + 1)
for i in range(M):
    for j in range(T, t[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - t[i]] + w[i])

print(dp[T])
