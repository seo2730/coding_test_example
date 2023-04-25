# 부품 찾기 p.199

# 계수 정렬
N = int(input())
count = [0]*1000001

for i in input().split():
    count[int(i)] = 1

M = int(input())
x = list(map(int,input().split()))

for i in x:
    if count[i] == 1:
        print('yes',end=' ')
    else:
        print('no',end=' ')