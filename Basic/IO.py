#genfromtxt로 데이터 가져오기
'''
두 개의 루프 실행
첫 번째 - 파일의 각 줄을 문자열 시퀀스로 변환
두 번째 - 각 문자열을 적절한 데이터 유형으로 변환
'''
import numpy as np
from io import StringIO

#Spitting the lines into columns/줄을 열로 나누기(csv는 ,로 구분)
data = u"1, 2, 3\n4, 5, 6"
#delimiter 분할기준
np.genfromtxt(StringIO(data), delimiter=",")

#다른 일반적인 구분 기호로 /t 표 문자. 기본적으로 delimeter=None행이 공백을 따라 분할되고, 
#delimeter 단일 정수 또는 정수 시퀀스로 설정
data = u"  1  2  3\n  4  5 67\n890123  4"
np.genfromtxt(StringIO(data), delimiter=3)

data = u"123456789\n   4  7 9\n   4567 9"
np.genfromtxt(StringIO(data), delimiter=(4, 3, 2)) #잘 모르겠다

#autostrip 인수 - 행이 일련의 문자열로 분해될 때 선행/후행 공백이 제거 안됨. autostrip를 값으로 설정하면 덮어쓰기 가능

data = u"1, abc , 2\n 3, xxx, 4"
np.genfromtxt(StringIO(data), delimiter=",", dtype="|U5")

np.genfromtxt(StringIO(data), delimiter=",", dtype="|U5", autostrip=True)

#comment 인수 - 주석의 시작을 표시하는 문자열 정의 #뒤에 있는 문자는 생략

data = u"""#
# Skip me !
# Skip me too !
1, 2
3, 4
5, 6 #This is the third line of the data
7, 8
# And here comes the last line
9, 0
"""
np.genfromtxt(StringIO(data), comments="#", delimiter=",")

#Skkiping lines and choosing colmns
#skip_header & skip_footer 인수 - 파일에 헤더가 있으면 데이터 처리에 방해가 되므로 건너뜀 가능

data = u"\n".join(str(i) for i in range(10))
np.genfromtxt(StringIO(data),skip_header=3, skip_footer=5) #앞3개 뒤5개 생략

#usecols 인수 - 가져올 열을 선택 가능
data = u"1 2 3\n4 5 6"
np.genfromtxt(StringIO(data), usecols=(0, -1)) #첫 번째 & 마지막 열

np.genfromtxt(StringIO(data), names="a, b, c", usecols=("a", "c")) #쉼표로 구분된 문자열로 지정하여 가져올수 있음

#Choosing data type

"""
파일에서 읽은 문자열이 다른 유형으로 변환되는 방식을 제어하는 주요 방법은 dtype 인수 설정
- dtype-float : names 인수를 사용하여 각 열과 연결되지 않은 경우 출력은 지정된 dtype 2D,
  문자열은 bool로 변환할수 있는지 확인부터 시작, 그 이후 정수, 부동 소수점, 복소수, 문자열로 변환 가능 - StringConverter 클레스 매퍼 수정
- .dtype=(int, float, float)
- 쉼표로 구분 된 문자열 dtype="i4,f8,|U3".
- 두 개의 키 'names'와 'formats'.
- 튜플 .(name, type)dtype=[('A', int), ('B', float)]
- 기존 numpy.dtype개체
"""

#Setting the name
#names 인수 - 테이블 형식 데이터를 처리할 때 자연스러운 접근 방식은 각 열에 이름을 할당하는 것, dtype 사용

data = u"1 2 3\n 4 5 6"
np.genfromtxt(StringIO(data), dtype=[(_, int) for _ in "abc"])
np.genfromtxt(StringIO(data), names="A, B, C")

data = u"So it goes\n#a b c\n1 2 3\n 4 5 6"
np.genfromtxt(StringIO(data), skip_header=1, names=True)

data = u"1 2 3\n 4 5 6"
ndtype=[('a',int), ('b', float), ('c', int)]
names = ["A", "B", "C"]
np.genfromtxt(StringIO(data), names=names, dtype=ndtype)

#defaultfmt인수 - names-None인 경우 그러나 dtype이 예상되고, "이름이 표준 numpy와 f%1"과 같은 이름으로 정의된다

data = u"1 2 3\n 4 5 6"
np.genfromtxt(StringIO(data), dtype=(int, float, int))
np.genfromtxt(StringIO(data), dtype=(int, float, int), names="a") #하나만 a 이후f0 f1
np.genfromtxt(StringIO(data), dtype=(int, float, int), defaultfmt="var_%02i") #이름 var_형태, 일부이름이 예상가지만 정의되지 않은 경우에만 사용

#Validating names / 이름 확인
"""
구조화된 dtype이 있는 numpy배열은 recarray로 볼 수 있다.
여기서 필드는 속성처럼 엑세스 가능하고, 필드이름에 오류가 있는지, 표준 속성(size & shape)과 일치 하지 않는지 확인해야 한다.
"""

#deletechars - 이름에서 삭제해야 하는 모든 문자를 결합한 문자열 ex)~!@#$%^&*()-=+~\|]}[{';: /?.>,<

#excludelist - 제외할 이름 목록 제공한다. 입력이름중 하나가 이 목록의 일부일 경우 '_'가 추가된다 ex)return, file, print...

#case_sensitive - 이름이 대소문자를 구분(case_sensitive=True)해야 하는지,
                  #대문자/소문자(case_sensitive=False | case_sensitive='upper')/(case_sensitive='lower')로 변환해야 하는지에 대한 여부
  
  
#Tweaking the conversion / 변환 조정  
#converters 인수 - 문자열에 추가 제어가 필요할때 사용 ex)YYYY/MM/DD가 datatime객체로 변환되는지 확인, xx%가 0~1사이의 부동소수점으로 변환되는지 확인

convertfunc = lambda x: float(x.strip(b"%"))/100.
data = u"1, 2.3%, 45.\n6, 78.9%, 0"
names = ("i", "p", "n")
np.genfromtxt(StringIO(data), delimiter=",", names=names) #두번째 열 nan
np.genfromtxt(StringIO(data), delimiter=",", names=names, converters={1: convertfunc}) #부동소수점
np.genfromtxt(StringIO(data), delimiter=",", names=names, converters={"p": convertfunc}) #위와 같음

convertfunc = lambda x: float(x.strip(b"%")) / 100.
data = u"1, , 3\n 4, 5, 6"
convert = lambda x: float(x.strip() or -999) #convert로 스트립된 문자열을 float로 변환하거나 비어있으면 -999
a = np.genfromtxt(StringIO(data), delimiter=",",converters={1: convert})

#Using missing and filling values / 누락 및 채우기 값 사용
"""
가져오려는 데이터 셋에 누락된 항목이 있을수도 있다. missing_values인수로 누락된 데이터를 인식하고 filling_values은 누락된 데이터를 처리한다.
"""

#missing_values - 기본적으로 빈 문자열은 누락된 것으로 표시된다.
                  #이 인수는 값의 문자열 또는 쉼표로 구분된 문자열 / 문자열의 시퀀스 / 딕셔너리를 받아 들인다.

#filling_values - 누락된 항목에 대한 값을 제공하며 dtype에서 결정된다
                  #bool - False / int - -1 / float - np.nan / complex - np.nan+0j/ string - '???'/ 단일 값, 일련의 값, 딕셔녀리 허용
  
data = u"N/A, 2, 3\n4, ,???"
kwargs = dict(delimiter=",",dtype=int,names="a,b,c",missing_values={0:"N/A", 'b':" ", 2:"???"},filling_values={0:0, 'b':0, 2:-999})
a = np.genfromtxt(StringIO(data), **kwargs)

#usemask
"""
True데이터가 누락된 항목과 나머지 False으로 추적한다. 출력배열은 MaskedArray
"""

#Shortcut functions / 바로가기 기능
"""
numpy.lib.npyio 모듈로부터 기능 제공한다.

-recfromtxt : 표준 numpy.recarray(if usemask=False) 또는 MaskedRecords배열(if usemaske=True)을 반환합니다 .
              기본 dtype은 dtype=None각 열의 유형이 자동으로 결정됨을 의미합니다.

-recfromcsv : recfromtxt와 같다.하지만 기본적으로 delimiter=",".

"""














