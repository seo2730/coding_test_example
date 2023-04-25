# 1이 될 때까지 p.99

N, M = map(int, input().split())

count = 0

while True:
    if (N%M) == 0:
        N = N/M
    else:
        N -= 1

    count += 1
    if N == 1:
        break

print(count)