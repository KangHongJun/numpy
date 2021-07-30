#Array types and conversions between types / 배열 유형 및 형변환
#기본유형 - https://numpy.org/doc/stable/user/basics.types.html'

import numpy as np

x = np.float32(1.0)
y = np.int_([1,2,4])
z = np.arange(3, dtype=np.uint8)

np.array([1, 2, 3], dtype='f')

z.astype(float) #astype로 형변환
np.int8(z) #일반적

d = np.dtype(int) #dtype출력
np.issubdtype(d, np.integer) #데이터 유형 판단

#Arrays Scalars

"""
numpy는 일반적으로 배열 요소를 배열 스칼라(연결된 dtype이 있는)로 반환.
배열 스칼라는 python 스칼라와 다르지만 대부분 서로 바꿔서 사용가능
구체적으로 스칼라를 확인해야할때 python 유형함수를 사용하여 배열 스칼라를 python 스칼라로 명시적으로 변환
"""

#Overflow Errors
np.power(100, 8, dtype=np.int64)
np.power(100, 8, dtype=np.int32)\
np.iinfo(int) #정수 & 부동소수점 최소값 최대값 제공, finfo도 있다곤 함

np.power(100, 100, dtype=np.int64) #부동소수점 숫자도 캐스팅될 수 있음
np.power(100, 100, dtype=np.float64)

#Extended Precision / 확장된 정밀도
  
""" 정
파이썬의 부동 소수점 숫자는 일반적으로 64비트 부동 소수점 숫자이며 거의 np.float64. 일부 특이한 상황에서는 부동 소수점 숫자를 더 정확하게 사용하는 것이 유용할 수 있습니다. 
이것이 numpy에서 가능한지 여부는 하드웨어와 개발 환경에 따라 다릅니다. 특히 x86 시스템은 80비트 정밀도의 하드웨어 부동 소수점을 제공하고 대부분의 C 컴파일러는 이를 유형 으로 제공 하지만 
MSVC(Windows 빌드용 표준)는 (64비트)와 동일합니다 . NumPy는 컴파일러 를 (및 복소수에 대해) 사용할 수 있도록 합니다 . numpy가 제공하는 것을 찾을 수 있습니다 
.long doublelong doubledoublelong doublenp.longdoublenp.clongdoublenp.finfo(np.longdouble)

NumPy는 C보다 더 정확한 dtype을 제공하지 않습니다 . 특히 128비트 IEEE 쿼드 정밀도 데이터 유형(FORTRAN의 \)은 사용할 수 없습니다.long doubleREAL*16

효율적인 메모리 정렬을 위해 np.longdouble일반적으로 0비트(96 또는 128비트)로 채워 저장됩니다. 어느 쪽이 더 효율적인지는 하드웨어와 개발 환경에 따라 다릅니다.
일반적으로 32비트 시스템에서는 96비트로 채워지는 반면 64비트 시스템에서는 일반적으로 128비트로 채워집니다. np.longdouble시스템 기본값으로 채워집니다. 
np.float96및 np.float128특정 패딩을 원하는 사용자를 위해 제공된다. 이름에도 불구하고, np.float96그리고 np.float128만큼만 정밀도로 제공 np.longdouble,
표준 Windows에서 대부분의 x86 시스템에서 80 비트와 64 비트 빌드입니다.

np.longdouble파이썬보다 더 높은 정밀도를 제공 하더라도 float파이썬은 종종 값을 강제로 통과시키므로 추가 정밀도를 잃기 쉽습니다 float. 
예를 들어, %형식화 연산자는 인수가 표준 파이썬 유형으로 변환되어야 하므로 많은 소수 자릿수가 요청되더라도 확장 정밀도를 유지하는 것은 불가능합니다.
값으로 코드를 테스트하는 것이 유용할 수 있습니다 .1 + np.finfo(np.longdouble).eps

"""






