#Converting python sequence numpy arrays

a1D = np.array([1, 2, 3, 4])
a2D = np.array([[1, 2], [3, 4]])
a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

a = np.array([127, 128, 129], dtype=np.int8)

a = np.array([2, 3, 4], dtype = np.uint32)
b = np.array([5, 6, 7], dtype = np.uint32)
c_unsigned32 = a - b #이상한값 나옴 둘중하나 .astype(np.int32) 형변환하여 연산

#Intinsic numpy array create function

#1D
np.arange(2, 10, dtype=float)
#0.1 씩
np.arange(2, 3, 0.1)
#6등분
np.linspace(1., 4., 6)

#2D
#단위행렬 생성
np.eye(3)
np.eye(3,5) #위와 같고 나머지 4,5열은 모두 0

#대각으로 수 넣음
np.diag([1, 2, 3])
np.diag([1, 2, 3], 1) #위와 같고 하단 1행 추가(모두 0)
np.vander([1, 2, 3, 4], 4)# 1행과 4열 1으로, 3열 1,2,3,4 2열은 3열의 제곱 1열은 3열의 3제곱

#3D
np.zeros((2, 3, 2))
default_rng(42).random((2,3,2))
np.indices((3,3))# 000,111,222 , 012,012,012

#replicating, joining, mutating existing arrays

a = np.array([1, 2, 3, 4, 5, 6])
b = a[:2]

b = a[:2].copy()

A = np.ones((2, 2))
B = np.eye((2, 2))
C = np.zeros((2, 2))
D = np.diag((-3, -4))
np.block([[A, B],[C, D]]) #4 4 배열로 결합

#read where disk

#use library HDF5: h5py FITS: Astropy

#ASCII
cat simple.csv
np.loadtxt('simple.csv', delimiter = ',', skiprows = 1) 

#Creating arrays from raw byte use of strings or buffera
#I/O 라이브러리 작성, fromfile()함수와 .tofile()메소드 사용

#Use special libray function(e.g, Scipy, Pandas, OpenCV)














