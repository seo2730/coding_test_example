# 효율적인 화폐 p.226

N,M = map(int,input().split())

money = []
for i in range(N):
    money.append(int(input()))

d = [10001]*(M+1)

# 다이나믹 프로그래밍 진행 (보텀업)
d[0] = 0
for i in range(N):
    for j in range(money[i],M+1):
        if d[j-money[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j],d[j-money[i]]+1)

if d[M] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[M])

