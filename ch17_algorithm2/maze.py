# 로봇이 미로의 입구(0, 0)에서 출발하여 출구(5, 5)를 향해 탐색합니다. 
# 갈림길이 나오면 한 방향으로 끝까지 가보고, 막다른 길이면 되돌아오는 방식으로 탐색합니다.

# DFS
# 범위 (0,0) ~ (5,5)
maze = [
    [0,1,1,1,1,1],
    [0,1,0,0,0,1],
    [0,1,0,1,0,1],
    [0,1,0,1,0,0],
    [0,0,0,1,1,0],
    [1,1,1,1,1,0]
]
# (0,0) => (0,1) #오른쪽 이동
# (0,0) => (0,-1) #왼쪽 이동
# (0,0) => (1,0) # 아래 이동
# (0,0) => (-1,0) # 위 이동

stack = []
visited = []
start = (0,0)
stack.append(start)
while stack:
    r, c = stack.pop()
    if 0 <= r <= 5 and 0 <= c <= 5:
        if (r,c) not in visited and maze[r][c] == 0: # 방문 리스트에 좌표가 없다면? 좌표 방문처리 및 스택에 인접노드 추가
            visited.append((r,c))
            stack.append((r+1,c))
            stack.append((r-1,c))
            stack.append((r,c+1))
            stack.append((r,c-1))
print(visited)

def solve_maze(maze, start):
    stack = []
    visited = []
    stack.append(start)
    while stack:
        r, c = stack.pop() # 방문 예정 좌표를 꺼냄
        """ 방문표시를 이렇게 할 수도 있음
        if maze[r][c] == 0:
            maze[r][c] = 2 
        """
        

        # 방문 리스트에 좌표가 없다면? 좌표 방문처리 및 스택에 인접노드 추가
        if (r,c) not in visited:
            visited.append((r,c))
            # 상,하,좌,우 탐색(미로 범위 내, 길(0)인 경우만 방문 예정 스택에 삽입)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                # 범위 -> 열(nc): 0~5 / 행(nr): 0~5
                if 0 <= nc < 6 and 0 <= nr < 6 and maze[nr][nc] == 0:
                    stack.append((nr, nc))
        
    return visited

print(solve_maze(maze, (0,0)))











