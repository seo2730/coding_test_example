# 두 배열의 원소 교체 p.182

N,K = map(int,input().split())

array = []
for i in range(2):
    array.append(list(map(int,input().split())))


A = sorted(array[0])
B = sorted(array[1],reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i],B[i] = B[i],A[i]
    else:
        break

print(sum(A))