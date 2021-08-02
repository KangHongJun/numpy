#Introduction to byte ordering and ndarrays / 바이트 순서 및 ndarrays소개 ..이 부분은 거의 이해 못함
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

"""
배열의 바이트 순서와 그것이 보고 있는(가리키는?) 기본 메모리 사이의 관계에 영향을 줄 수 있는 두 가지 방법이 있다.
1. 기본 데이터를 다른 바이트 순서로 해석하도록 dtype의 바이트 순서 정보를 변경 - arr.newbyteorder()
2. dtype 해석을 그대로 두고 기본 데이터의 바이트 순서를 변경 - arr.byteswap()

바이트 순서를 변경하는 경우는 3가지가 있다,
"""

#데이터와 dtype 엔디안이 일치하지 않습니다. 데이터와 일치하도록 dtype을 변경

big_end_buffer = bytearray([0,1,3,2])
#일치하지 않는것 만들기
wrong_end_dtype_arr = np.ndarray(shape=(2,),dtype='<i2', buffer=big_end_buffer) #위에선 빅 엔디안 여기에선 리틀 엔디안을 하여 값이 달라진듯함

fixed_end_dtype_arr = wrong_end_dtype_arr.newbyteorder() #방법 1번 사용
fixed_end_dtype_arr.tobytes() == big_end_buffer #수정된걸 비교해보면 True

#데이터 및 유형 엔디안이 일치하지 않습니다. 데이터를 일치하는 유형으로 변경
#특정 순서가 되도록 메모리의 데이터가 필요한 경우 가능. 특정 바이트 순서가 필요한 파일에 메모리를 쓸 수 있음.
fixed_end_mem_arr = wrong_end_dtype_arr.byteswap()#바이트 순서 변경

fixed_end_mem_arr.tobytes() == big_end_buffer # False

#데이터 및 dtype 엔디안 일치, 데이터 및 dtype 스왑
#올바르게 지정된 배열 dtype이 있을 수 있지만 배열이 메모리에서 반대 바이트 순서를 가져야하며, 배열 값이 의미가 있도록 dtype 일치를 원함

ig_end_buffer = bytearray([0,1,3,2])

big_end_arr = np.ndarray(shape=(2,),dtype='>i2', buffer=big_end_buffer)
swapped_end_arr.tobytes() == big_end_buffer #False

swapped_end_arr = big_end_arr.astype('<i2')
swapped_end_arr.tobytes() == big_end_buffer # False

