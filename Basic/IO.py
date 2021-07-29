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

ata = u"1, abc , 2\n 3, xxx, 4"
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

#





