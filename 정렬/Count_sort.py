# 계수 정렬 p.171

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array)+1)

n = len(array)
for i in range(n):
    # 각 데이터에 해당되는 index의 값 증가
    count[array[i]] += 1

m = len(count)
for i in range(m):
    for j in range(count[i]):
        # 띄어쓰기를 구분으로 등장한 횟수만큼 index 출력
        print(i,end=' ')