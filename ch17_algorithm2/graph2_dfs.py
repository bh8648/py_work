# graph2_dfs.py

"""
DFS 동작 방식 : stack
-> 2개의 공간이 필요(방문할 노드를 담음, 방문했는지 체크)

1. 방문(탐색)할 노드를 담을 스택(Stack) 자료형 생성
2. 각 노드가 방문한 노드인지를 체크하는 리스트 생성
3. 탐색 시작 노드(첫 방문 노드)를 스택에 삽입
4. 방문할 노드를 스택에서 하나씩 꺼내기
5. 스택에서 꺼낸 노드가 방문한 노드가 아니면,
    꺼낸 노드의 인접 노드를 스택에 삽입하고 방문 처리
6. 스택에 방문할 노드가 남지 않을 때까지 4~5의 과정을 반복
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

def my_dfs(graph, start_node):
    # 1. 방문(탐색)할 노드를 담을 스택(Stack) 자료형 생성
    stack = list()
    # 2. 각 노드가 방문한 노드인지를 체크하는 리스트 생성
    visited = list()
    # 3. 탐색 시작 노드(첫 방문 노드)를 스택에 삽입
    stack.append(start_node)

    # 6. 4~5번을 계속 반복
    while stack:
        # 4. 방문할 노드를 스택에서 하나씩 꺼내기
        node = stack.pop()
        # 5. 스택에서 꺼낸 노드가 방문한 노드가 아니면,
        #     꺼낸 노드의 인접 노드를 스택에 삽입하고 방문 처리    
        #     reversed() 사용시, 리스트 순서를 반대로 설정 stack에 넣으면 후입선출이기 때문에 보기좋게 만들려고 reversed() 사용해서 뒤집어서 집어넣기    
        if node not in visited:
            visited.append(node) # 1. 방문처리
            stack.extend(reversed(graph[node])) # 2. 인접노드를 스택에 추가
            print(f"Visited={visited}")
            print(f"    Stack={stack}")

    return visited
print(my_dfs(undirected_graph1, "A"))