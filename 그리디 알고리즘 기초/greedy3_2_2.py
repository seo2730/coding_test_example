# 큰 수의 법칙 p.92

# 가장 큰 수와 두 번째로 큰 수만 이용하므로 일정 규칙 이용해서 풀 수 있음

N,M,K = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first=data[N-1]
second=data[N-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(M/(K+1))*K # K+1 : 가장 큰 수 더하는 횟수 + 두 번째 큰 수 한번 -> 반복 횟수 x 가장 큰 수 더하는 횟수
count += M%(K+1) # 반복하고 남은 횟수에서 가장 큰 수 더하는 횟수

result = 0
result += count * first
result += (M-count)*second

print(result)