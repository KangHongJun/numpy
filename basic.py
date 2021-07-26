import numpy as np
from numpy import newaxis

#기본 배열
np.array([1,2,3])
#zeros, ones, empty 0, 1, 초기화 안된 값

#10 ~ 30미만까지 5씩
np.arange(10,30,5)

A = np.array([[1, 1], [2, 1]])
B = np.array([[1, 1], [4, 1]])
#행렬곱 
A@B | A.dot(B)

#난수 생성기
rg = np.random.default_rng(1)

#0~6 3등분
np.linspace(0, 6, 3)

#랜덤 2,3배열
rg.random((2,3))

#0~11(12개) 3,4배열
C = np.arange(12).reshape(3, 4)

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



