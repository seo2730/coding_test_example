# 1이 될 때까지 p.99

N, M = map(int, input().split())

remain = 0
result = N 
count = 0

while True:
    if (result//M) != 0:
        remain += (result%M)
    else:
        remain += (result%M) - 1
        break
    
    result = result//M
    
    count += 1

count += remain
print(count)
