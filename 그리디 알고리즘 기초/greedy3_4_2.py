# 1이 될 때까지 p.99

N, M = map(int, input().split())

remain = 0
result = N 
count = 0

while True:
    if (result%M) != 0 and result!=1:
        remain = (result%M)
    
    result = result//M
    
    count += 1

    if result == 1:
        break

count += remain
print(count)