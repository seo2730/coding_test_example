# 위에서 아래로 p.178

N = int(input())

array = []
for i in range(N):
    array.append(int(input()))

array = sorted(array,reverse=True)

for i in range(N):
    print(array[i],end=' ')