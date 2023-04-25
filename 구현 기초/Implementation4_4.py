# 게임 개발 p.118

N,M = map(int,input().split())
x,y,w = map(int,input().split())

# 맵 생성
maps = []
for i in range(N):
    maps.append(list(map(int,input().split())))

# 방문한 곳 처리 : 방문하면 1 안하면 0
d = [[0]*M for _ in range(N)]
# 현재 좌표는 방문으로 처리
d[x][y] = 1

# 북 동 남 서 정의 : 문제에서 왼쪽으로 회전하므로 이렇게 순서를 줌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 회전
def turn_left():
    global w
    w -= 1
    if w == -1:
        w=3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[w]
    ny = y + dy[w]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하거나 육지인 경우 이동
    if d[nx][ny] == 0 and maps[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 간 칸이거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[w]
        ny = y - dy[w]
        # 뒤로 갈 수 있다면 이동하기
        if maps[nx][ny] == 0:
            x = nx
            y = ny
        # 바다일 경우
        else:
            break
        turn_time = 0
        
print(count)