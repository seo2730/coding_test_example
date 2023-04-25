# 숫자카드 게임 p.98

N,M = map(int,input().split())

min_list = []
for i in range(N):
    min_list.append(min(list(map(int,input().split()))))

print(max(min_list))

