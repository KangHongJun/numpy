#Introduce
#구조적 배열은 데이터 유형이 명명된 필드의 시퀀스로 구성된 단순한 데이터 유형의 조합인 ndarray

x = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)],dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
"""
이는 데이터 유형이 3개의 필드가 있는 구조인 길이2의 1차원 배열이다 name이라는 문자열 길이 10이하, age라는 32비트 정수, weight라는 비트부동소수점
"""
x[1]
x['age']
x['age']=5 #age 값 바뀜
"""
구조화된 데이터 유형은 c언어의 구조체를 모방하고 유사한 메모리 레이아웃을 공유할수 있도록 설계되엇다. 
C코드와 인터페이스하고 구조화된 버퍼의 저수준 조건을 위한 것이다.
"""

#Structured Datatypes / 구조화된 데이터 유형

"""
구조화된 데이터 유형은 필드 모음으로 해석되는 특정 길이의 바이트 시퀀스로 생각할 수 있다.
각 필드에는 구조 내에서 이름, 데이터 유형 및 바이트 오프셋이 있다.
필드의 데이터 유형은 다른 구조화된 데이터 유형을 포함한 모든 numpy게이터 유형일 수 있고
지정된 모양의 ndarray처럼 동작하는 하위 배열 데이터 유형일수도 있다.
필드의 오프셋은 임의적이며 필드가 겹칠 수도 있다.
이러한 오프셋은 일반적으로 numpy에 의해 자동으로 결정되지만 지정도 가능하다
"""

#Creation

#1. 튜플 목록, 필드당 하나의 튜플
"""
각 튜플은 모양이 선택사항인 형식을 갖는다. 문자열이고 데이터 유형으로 변환될 수 있는 모든 개체 일 수 있으며
하위 배열 모양을 지정하는 정수의 튜플이다. 
"""
np.dtype([('x', 'f4'), ('y', np.float32), ('z', 'f4', (2, 2))])

np.dtype([('x', 'f4'), ('', 'i4'), ('z', 'i8')]) # 이름이 비여있으면 필드 형식의 기본 이름 부여

#2. 쉼표로 구분된 dtype문자열
"""
문자열 dtype 사양은 문자열에서 사용할 수 있으며 쉼표로 구분할 수 있다.
필드의 itemsize 바이트 오프셋은 자동으로 결정, 필드이름은 기본 이름 부여
"""
np.dtype('i8, f4, S3') #이름 f0부터 자동 부여
np.dtype('3int8, float32, (2, 3)float64') #이름 f0부터 자동부여, 바이트 오프셋 자동결정

#3. 필드 매개변수 배열 사전
"""
필드의 바이트 오프셋과 구조의 항목 크기를 제어할 수 있기 때문에 가장 유연한 사양 형식

사전에는 'names' 및 'formats' 라는 두 개의 필수키와 'itemsize', 'aligned', 'titles'라는 4개의 선택적 키가 있다.
"""

#4. 필드 이름 사전
"""
이 형식의 사양을 사용하는 것은 권장되지 않지만 이전 numpy 코드에서 사용할 수 있음
사전의 키는 피르디름이고 같은 유형과 오프셋 지정하는 튜플
"""
np.dtype({'col1': ('i1', 0), 'col2': ('f4', 1)}) #권장되지는 않음

#구조화된 데이터 유형 조작 및 표시 - 필드 이름 목록은 names dtype객체의 속성에서 찾을수 있음.
d  = np.dtype([('x', 'i8'), ('y', 'f4')])
d.names

"""
필드이름은 names와 동일한 길이의 문자열 시퀀스를 사용하여 속성에 할당하여 수정가능

dtype객체는 딕셔너리와 유사한 속성을 가지고 fileds키가 필드이름이고 값이 각 필드의 dtype 및 바이트 오프셋을 포함하는 튜플
"""
d.fields

#자동 바이트 오프셋 및 정렬

"""
numpy는 align=True에 대한 키워드 인수로 지정 되었는지 여부에 따라 두가지 방법중 하나를 사용하여
구조화된 대이터유형의 필드 바이트 오프셋과 전체 항목 크기를 자동으로 결정

기본적으로(align=False) numpy는 각 필드가 이전 필드가 끝난  바이트 오프셋에서 시작하고 필드가 메모리에서 연속되도록 함께 묶는다.
"""

def print_offsets(d):
  print("offsets:", [d.fields[name][1] for name in d.names])
  print("itemsize:", d.itemsize)
print_offsets(np.dtype('u1, u1, i4, u1, i8, u2'))
"""
align=True 경우 많은 C 컴파일러 패드는 C구조체를 하는것과 같은 방식으로 numpy와 의지패드에게 구조를 설정한다.
정렬된 구조는 경우에 따라 데이터 유형의 크기가 증가하는 대신 기능향상을 제공한다.
패딩 바이트는 각 필디의 바이트 오프셋이 해당 필드 정렬의 베수가 되도록 필드 사이에 삽입되며,
이는 일반적으로 단순 데이터 유형일 경우 바이트 단위 필드 크기와 같다.
구조에는 항목 크기가 가장 큰 정렬의 배수가 되도록 후행 패딩도 추가한다.
"""
print_offsets(np.dtype('u1, u1, i4, u1, i8, u2', align=True))












