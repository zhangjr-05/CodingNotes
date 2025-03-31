# 有一个国家包含N个城市和M条道路 每条道路连接两个城市 并且有一个非负的权重表示道路的长度
# 给定一个起始城市S和一个目标城市T 请找到从城市S到城市T的最短路径 并输出路径长度。

edges = [
    ['a', 'b', 7],
    ['a', 'c', 8],
    ['a', 'd', 2],
    ['a', 'g', 4],
    ['b', 'c', 1],
    ['b', 'e', 2],
    ['b', 'h', 3],
    ['c', 'd', 4],
    ['c', 'e', 2],
    ['c', 'f', 7],
    ['d', 'f', 3],
    ['d', 'g', 5],
    ['e', 'f', 4],
    ['e', 'h', 1],
    ['f', 'g', 4],
    ['f', 'h', 3],
    ['g', 'h', 6]
]

import heapq    # 小顶堆

def Dijkstra(start, end):
    # 构建图
    graph = {}
    for u, v, w in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, w))
        graph[v].append((u, w))

    pq = [(0, start)]
    come_from = {start: None}
    memo = {city: float('inf') for city in graph}
    memo[start] = 0

    while pq:
        d, city = heapq.heappop(pq)
        if city == end:
            path = []
            current = city
            while current:
                path.append(current)
                current = come_from[current]
            return path[::-1], d
        
        for v, w in graph[city]:
            if d + w < memo[v]:
                heapq.heappush(pq, (d + w, v))
                memo[v] = d + w
                come_from[v] = city

    return None, -1


start, end = input("输入起始城市和目标城市: ").split()

path, length = Dijkstra(start, end)

print(f"途径城市 {path}")
print(f"最短路径长度为 {length}")