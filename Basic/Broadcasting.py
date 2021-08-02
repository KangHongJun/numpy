"""
브로드캐스팅은 산술 연산 중에 numpy가 다른 모양의 배열을 처리하는 방법.
특정 제약 조건에 따라 더 작은 배열은 호환되는 모양을 갖도록 더 큰 배열에 걸쳐 브로드캐스트 된다.
배열 연산을 벡터화하는 수단을 제공하여 python대신 c에서 루프가 발생하도록 함
데이터 복사본을 만들지 않고 수행하여 일반적으로 효율적인 알고리즘 구현으로 이어지지만, 계산을 느리게 하는 비효율적인 메모리 사용으로 이어짐
"""

import numpy as np

#일반적인 상황(배열 모양 같음)
a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
a*b 

#위의 예제와 결과가 같고, 더 효율적임.
c=2.0
a*c

#General Broadcasting Rules(일반 방송 규칙)
"""
두 개의 배열에서 작업할 때 numpy는 요소별로 모양을 비교, 오른쪽 차원에서 왼쪽으로 작동하고
그 둘이 동등하거나, 둘 중 하나가 1이면 호환된다.
조건이 충족되지 않으면 호환불가 예외 발생

#배열의 차원수가 같을 필요는 없다 256x256x3 RGB 값의 배열이 있고, 이미지의 각 색상을 다른값으로 조장하려는 경우 이미지에 3개의 값이 있는
1차원 배열을 곱할 수 있다. 브로드캐스트 규칙에 따라 배열의 후행 축 크기를 정렬하면 호환가능.
"""

"""
Image  (3d array): 256 x 256 x 3
Scale  (1d array):             3
Result (3d array): 256 x 256 x 3
"""

#비교된 차원 중 하나가 하나이면 다른차원이 사용됨 즉 다른 크기가 1인 치수는 다른 치수와 일치하도록 늘어나거나 복사됨
"""
A      (4d array):  8 x 1 x 6 x 1
B      (3d array):      7 x 1 x 5
Result (4d array):  8 x 7 x 6 x 5

A      (2d array):  5 x 4
B      (1d array):      1
Result (2d array):  5 x 4

A      (2d array):  5 x 4
B      (1d array):      4
Result (2d array):  5 x 4

A      (3d array):  15 x 3 x 5
B      (3d array):  15 x 1 x 5
Result (3d array):  15 x 3 x 5

A      (3d array):  15 x 3 x 5
B      (2d array):       3 x 5
Result (3d array):  15 x 3 x 5

A      (3d array):  15 x 3 x 5
B      (2d array):       3 x 1
Result (3d array):  15 x 3 x 5

브로드캐스트 못하는 모양
A      (1d array):  3
B      (1d array):  4 # trailing dimensions do not match

A      (2d array):      2 x 1
B      (3d array):  8 x 4 x 3 # second from last dimensions mismatched
"""

#코드 예시
x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)
z = np.ones((3,4))

x+y #에러
xx+y
x+z
xx+z #에러


a = np.array([0.0, 10.0, 20.0, 30.0])
b = np.array([1.0, 2.0, 3.0])
a+b #에러
a[:, np.newaxis] + b #a를 4행 형태로 바꾸고 연산


