# graph1.py


undirected_graph1 = {
    "A":["B", "C", "D"],
    "B":["A", "E"],
    "C":["A", "F", "G"], 
    "D":["A", "H"], 
    "E":["B", "I"], 
    "F":["C", "J"], 
    "G":["C"], 
    "H":["D"], 
    "I":["E"], 
    "J":["F"]
}

directed_graph1 = {
    "A":["B", "C", "D"],
    "B":["E"],
    "C":["F", "G"], 
    "D":["H"], 
    "E":["I"], 
    "F":["J"], 
    "G":[], 
    "H":[], 
    "I":[], 
    "J":[]
}


undirected_graph2 = {
    1:[2,3,4],
    2:[1,5],
    3:[1,6],
    4:[1,6],
    5:[2,6],
    6:[3,4,5],
}
# 예상 결과:
# dfs -> 1,2,5,6,3,4
# bfs -> 1,2,3,4,5,6

def dfs(graph, start_node):
    stack = []
    visited = []
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    return visited
print(dfs(undirected_graph2, 1))

def bfs(graph, start_node):
    queue =[]
    visited = []
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited
print(bfs(undirected_graph2, 1))




