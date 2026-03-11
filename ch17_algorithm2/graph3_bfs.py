# graph3_bfs.py

"""
BFS 동작 방식 : queue
-> dfs와 동작 방식은 같은데 stack이 아니라 queue로 할 뿐임

1. 방문(탐색)할 노드를 담을 큐(Queue) 자료형 생성
2. 각 노드가 방문한 노드인지를 구분할 수 있는 리스트 생성
3. 탐색 시작 노드(첫 번째 노드)를 큐에 삽입
4. 방문할 노드를 큐에서 하나씩 꺼내기(삽입된 순서대로)
5. 큐에서 꺼낸 노드가 방문한 노드가 아니면, 그 인접 노드를 큐에 삽입하고 방문 처리
6. 큐에 방문할 노드가 남지 않을 때까지 4~5의 과정을 계속 반복

"""
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

def my_bfs(graph, start_node):
    # 1. 방문할 노드를 담을 큐 생성
    queue = list()
    # 2. 방문한 노드를 담을 리스트 생성
    visited = list()
    # 3. 시작 노드를 큐에 삽입
    queue.append(start_node)

    # 6. 큐가 빌 때까지 4~5 반복
    while queue:
        # 4.  방문하려는 노드를 큐에서 꺼냄
        node = queue.pop(0)

        # 방문 하려는 노드를 방문한 적이 없다면? 해당 노드를 방문처리하고 인접 노드를 큐에 삽입
        if node not in visited:
            queue.extend(graph[node]) # 인접노드를 큐에 삽입
            visited.append(node) # 방문처리
            print(f"Visited={visited}")
            print(f"    Queue={queue}")
    
    return visited

print(my_bfs(undirected_graph1, 'A'))

print(my_bfs(undirected_graph1, 'I'))


