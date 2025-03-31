n, m, t = map(int, input().split())
sx, sy, fx, fy = map(int, input().split())
barriers = set()
for i in range(t):
    x, y = map(int, input().split())
    barriers.add((x, y))

ans = 0
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

valid = lambda x, y: 1 <= x <= n and 1 <= y <= m and (x, y) not in barriers

def dfs(x, y, memo):
    if (x, y) == (fx, fy):
        global ans
        ans += 1
        return
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if valid(nx, ny) and (nx, ny) not in memo:
            new_memo = memo.copy()
            new_memo.add((nx, ny))
            dfs(nx, ny, new_memo)


dfs(sx, sy, set([(sx, sy)]))

print(ans)