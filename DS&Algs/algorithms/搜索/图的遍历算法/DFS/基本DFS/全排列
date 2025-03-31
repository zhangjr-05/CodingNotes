def dfs(n):
    if len(path) == n:
        print(path)
        return
    for i in range(1, n + 1):
        if i not in path:
            path.append(i)
            dfs(n)
            path.pop()

n = int(input())
path = []
dfs(n)