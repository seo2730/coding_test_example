# 성적이 낮은 순서로 출력하기 p.180

N = int(input())

array = []
for i in range(N):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1])))

array = sorted(array,key=lambda x:x[1])

for i in range(N):
    print(array[i],end=' ')