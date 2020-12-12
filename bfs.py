from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]

visited = [False]*len(graph)

def bfs(graph, start, visited):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end= " ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

bfs(graph, 1, visited)