#Introduction to byte ordering and ndarrays / 바이트 순서 및 ndarrays소개
"""
ndarrays는 메모리 내의 파이썬 배열 인터페이스를 제공하는 것이 목적
배열로 보려는 메모리가 Python을 실행 중인 컴퓨터와 동일한 바이트 순서가 나닌 경우가 종종 있다.

예를 들어 "Intel Pentium과 같은 리틀 엔디안 CPU"가 있는 컴퓨터에서 작업하고 있지만 "빅 엔디안 컴퓨터에서 작성한 파일"에서 일부 데이터를 로드,
빅 엔디안 컴퓨터에서 작성한 파일에서 4바이트를 로드했다고 가정할 때, 이 4바이트가 2개의 16비트 정수를 나타낸다는것을 안다.
빅 엔디안 시스템에서 2바이트 정수는 먼저 MSB(Most Significant Byte)와 함계 저장되고 그 다음 LSB(Least Significant Byte)와 함께 저장된다.
따라서 바이트는 메몰 순서로 MSB 정수 1 -> LSB정수 2 -> MSB정수 2 -> LSB정수 2

두 정수가 실제로 1과 770이라고 가정하면 770 = 256 * 3 + 2 이므로
메모리의 4바이트에는 각각 0 1 3 2가 포함된다.
파일에서 로드한 바이트에는 다음 내용이 포함된다.
"""
big_end_buffer = bytearray([0,1,3,2]) #->bytearray(b'\\x00\\x01\\x03\\x02')
#>i2 : 빅 엔디안(<리틀), i2 = 2 바이트 정수, <u4 : 문자열, 단일 부호 없는 4바이트 리틀 엔디안 정수
#아무튼 770은 256*3 +2
big_end_arr = np.ndarray(shape=(2,),dtype='>i2', buffer=big_end_buffer) # ->big_end_arr[0] = 1, big_end_arr[1] = 770

little_end_u4 = np.ndarray(shape=(1,),dtype='<u4', buffer=big_end_buffer) #little_end_u = array([33751296], dtype=uint32)
little_end_u4[0] == 1 * 256**1 + 3 * 256**2 + 2 * 256**3

#스칼라는 현재 바이트 순서 정보를 포함하지 않으므로 배열에서 스칼라를 추출하면 기본 바이트 순서로 정수가 반환
big_end_arr[0].dtype.byteorder == little_end_u4[0].dtype.byteorder # 각각 dtype은 int16, 32이지만 byteorder하면 '='

#Changing byte ordering / 바이트 순서 변경

