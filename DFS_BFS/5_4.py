# 미로 탈출 p.152
from collections import deque

N,M = map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))

# 이동 방향(상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS 소스 구현
def bfs(x,y):
    # Queue 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))

    # Queue가 빌 때까지 반복
    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 네 방향 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록 -> 1이 아니면 queue를 안 넣음
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단거리 변환
    return graph[N-1][M-1]

print(bfs(0,0))