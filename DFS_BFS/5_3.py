# 음료수 얼려 먹기 p.149

N,M = map(int,input().split())

# 얼음 틀 정보 받아오기
graph = []
for i in range(N):
    # 맵 정보는 띄어져 있지 않으므로 split 함수 안 씀
    graph.append(list(map(int,input())))

# DFS로 특정 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y]=1
        #상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        # 스택 구조로 인해 마지막으로 true를 반환
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
print(graph)
for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1

print(result)