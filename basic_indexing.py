#Single element

x = np.arange(10)

x[2]
x[-2] #또는 2차원

#other option
x[2:5]
x[:-7]
y = np.arange(35).reshape(5,7)
y[1:5:2,::3]

#Index arrays

#정수유형, 각 값은 인덱스 대신 사용할 배열의 값
x - np.arange(10,1,-1)
x[np.array[3,3,1,8]]
x[np.array([[1,1],[2,3]])] #다차원 배열로도 가능

#Index multi-dimensional array
y = np.arange(35).reshape(5,7)
y[np.array([0,2,4]), np.array([0,1,2])]
y[np.array([0,2,4])] #행 기준

#booleBn or mask index arrays
b = y>20
y[b]
b[:,5]
y[b[:,5]]

x = np.arange(30).reshape(2,3,5)
b = np.array([[True, True, False], [False, True, True]])
x[b] #T인 부분만 출력되며 하나의 배열로

#combining index arrays with slices

y[np.array([0, 2, 4]), 1:3]
y[:, 1:3][np.array([0, 2, 4]), :] #위와 동일
y[b[:,5],1:3]

#Structural indexing tools

#배열 모양을 쉽게 일치시키기 위해 np.newaxis객체로 차원 추가
y.shape
y[:,np.newaxis,:].shape #차원만 증가

x = np.arange(5)
x[:,np.newaxis] + x[np.newaxis,:] #

#Assigning values to indexed arrays

x = np.arange(10)
x[2:7] = 1
x[2:7] = np.arange(5)
x[1] = 1.2

x = np.arange(0, 50, 10)
x[np.array([1, 1, 3, 1])] += 1

#Dealing with variable numbers of indices within programs

#다양한 인덱스를 처리할때 제한적이므로 이를 위해 인덱스에 튜플을 제공하면 튜플은 인덱스 목록으로 해석된다.

z = np.arange(81).reshape(3,3,3,3)
indices = (1,1,1,1)
z[indices]

indices = (1,1,1,slice(0,2))
z[indices]

indices = (1, Ellipsis, 1)

z[[1,1,1,1]] # 01번째부터 시작
z[(1,1,1,1)] #값
