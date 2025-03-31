def dfs(start):
    if len(path) == m:
        if sum(path) == n:
            print(path)
        return
    for i in range(start, n + 1):
        path.append(i)
        dfs(i)
        path.pop()
        
# 将n分解成n个正整数的和，打印所有解
n, m = map(int, input().split())
path = []
dfs(1)