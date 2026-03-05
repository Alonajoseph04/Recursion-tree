time = 0

graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'G', 'H'],
    'D': ['F'],
    'E': ['B', 'F'],
    'F': ['E'],
    'G': [],
    'H': ['A', 'C', 'G']
}

color = {}
parent = {}
discovery = {}
finish = {}

def dfs_visit(u):
    global time
    color[u] = "GRAY"
    time += 1
    discovery[u] = time

    for v in graph[u]:
        if color[v] == "WHITE":
            parent[v] = u
            print(f"{u} -> {v} : Tree Edge")
            dfs_visit(v)
        elif color[v] == "GRAY":
            print(f"{u} -> {v} : Back Edge")
        else:
            print(f"{u} -> {v} : Forward/Cross Edge")

    color[u] = "BLACK"
    time += 1
    finish[u] = time


def dfs():
    for v in graph:
        color[v] = "WHITE"
        parent[v] = None

    for v in graph:
        if color[v] == "WHITE":
            dfs_visit(v)


dfs()

print("\nVertex  Discovery  Finish")
for v in graph:
    print(v, discovery[v], finish[v])