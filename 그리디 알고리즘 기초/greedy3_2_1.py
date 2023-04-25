# 큰 수의 법칙 p.92

N,M,K = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first=data[N-1]
second=data[N-2]

result = 0

while True:
    for i in range(K): # 가장 큰 수를 K번 더하기
        if M==0:
            break
        result += first
        M-=1
    if M == 0:
        break
    result += second # 두 번째로 큰 수 한번 더하기
    M-=1

print(result)