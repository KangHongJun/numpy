import numpy as np
from numpy import newaxis

#기본 배열
np.array([1,2,3])
#zeros, ones, empty 0, 1, 초기화 안된 값

#10 ~ 30미만까지 5씩
np.arange(10,30,5)
#정렬
np.sort()

A = np.array([[1, 1], [2, 1]])
B = np.array([[1, 1], [4, 1]])

#배열 연결
np.concatenate((A, B))

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
#axis=0 없어도 되긴함
np.concatenate((x, y), axis=0)


#행렬곱 
A@B | A.dot(B)

#난수 생성기
rg = np.random.default_rng(1)
ng.integers(5, size=(2, 4)) #0~4이하의 값으로 2,4배열에 랜덤

#0~6 3등분
np.linspace(0, 6, 3)

#랜덤 2,3배열
rg.random((2,3))

#0~11(12개) 3,4배열
C = np.arange(12).reshape(3, 4)

#ndlm 차원 수, size 요소 수, shape 모양
#sum, min, max, axis-0은 행, 1은 열, exp, sqrt

a = np.floor(10 * rg.random((2, 2)))
b = np.floor(10 * rg.random((2, 2)))

#1행으로 배열
a.ravel()
#(6,2)로 재배열, resize 가능, 차원하나 설정되면 나머지 자동
a.reshape((6,2))
#행렬 반전
a.T

#배열 쌓기(행 방향)
np.vstack((a, b))
#배열 쌓기 (열 방향)
np.hstack((a, b))

#배열 쌓기(열 방향)
np.column_stack((a, b))

c = np.array([4., 2.])
d = np.array([3., 8.])
#배열을 열로 쌓음
np.column_stack((a, b))
->array([[4., 3.],
       [2., 8.]])

#배열 나누기
e = np.floor(10 * rg.random((2, 12)))
#배열 a를 배열 3개로 나눔
np.hsplit(a, 3)
#잘 모르겠다
np.hsplit(a, 3, 4)

#얕은 복사 주의
f=a #주소가 같다
f=a.view() #주소 다름
#deep copy
g = a.copy()

a = np.arange(12)**2
i = np.array([1, 1, 3, 8, 5])
j = np.array([[3, 4], [9, 7]])
#함수에 넣듯이 i의 제곱수들이 나옴- [조건]
a[i] 
a[i]


palette = np.array([[0, 0, 0],[255, 0, 0], [0, 255, 0],[0, 0, 255], [255, 255, 255]]) 
image = np.array([0,1,4,4])
#image의 값 각각 대입->0이면 모두0, 수의 위치에 255, 4일 경우엔 모두255
palette[image]

a = np.arange(12).reshape(3, 4)
i = np.array([[0, 1], [1,2]])
j = np.array([[2, 1],[3,3]])
l = (i, j)
#a[0,2], a[1,1]
#a[1,3], a[3,3]
a[i,j] #a[l]

a = np.arange(12).reshape(3, 4)
b1 = np.array([False, True, True])   
b2 = np.array([True, False, True, False])

#행기준 가장 작은값 위치 출력
argmax(axis=0)

time = np.linspace(20, 145, 5)
data = np.sin(np.arange(20)).reshape(5, 4)
ind = data.argmax(axis=0) #가장 큰 값의 위치

time_max=time[ind]#ind 값으로 정렬

ab = np.arange(5)
#특정위치 값 바꾸기
ab[[1, 3, 4]] = 0 #[1, 2, 3], += 1

#boolean
a = np.arange(12).reshape(3, 4)
b = a > 4 #T F 판별출력
a[b] #만족하는 배열 출력
a[b] = 0 #만족하는 부분 0으로

#벡터결합 np.ix_
a = np.array([2, 3, 4, 5])
b = np.array([8, 5, 4])
c = np.array([5, 4, 6, 8, 3])
ax, bx, cx = np.ix_(a, b, c)

#파일로 저장(csv 가능)
np.save('filename', a)
#파일 읽기
b = np.load('filename.npy')
print(b)




