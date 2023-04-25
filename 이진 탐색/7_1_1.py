# 부품 찾기 p.197

# 반복문 이용
def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end)//2

        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end = mid-1
        elif array[mid]<target:
            start = mid+1

    return None

N = int(input())
A = list(map(int,input().split()))
A.sort()

M = int(input())
B = list(map(int,input().split()))

for i in B:
    result = binary_search(A,i,0,N-1)
    if result == None:
        print('no',end=' ')
    else:
        print('yes',end=' ')