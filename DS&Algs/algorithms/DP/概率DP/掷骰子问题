# 掷一个六面骰子n次 计算得到点数和为target的概率

def dice_probability(n, target):
    # dp[i][j]: 投掷i次骰子 点数和为j的概率
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    # 状态转移
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            for k in range(1, 7):
                if j - k >= 0:
                    dp[i][j] += dp[i - 1][j - k] * (1 / 6)
    return dp[n][target]
