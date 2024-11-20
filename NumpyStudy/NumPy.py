import numpy as np
# # 使用标量类型
# dt = np.dtype(np.int32)
# print(dt)

# # int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
# dt = np.dtype('i4')
# print(dt)

# # 字节顺序标注
# dt = np.dtype('<i4')
# print(dt)

# dt = np.dtype([('age',np.int8)]) 
# print(dt)
# a = np.array([(10,),(20,),(30,)], dtype = dt) 
# print(a)
# print(a['age'])


# student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
# print(student)
# a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
# print(a)
# # ------------------------------------------------------------
# print('bytes ------------------------------------------------------------')
# # ndarray.ndim 用于获取数组的维度数量（即数组的轴数）。
# a = np.arange(24)  
# print (a.ndim)             # a 现只有一个维度
# # 现在调整其大小
# b = a.reshape(2,4,3)  # b 现在拥有三个维度
# print (b.ndim)
# # ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性(秩)
# a = np.array([[1,2,3],[4,5,6]])  
# print (a.shape)             # 输出 (2, 3)
# # ndarray.shape 也可以用于调整数组大小。
# a = np.array([[1,2,3],[4,5,6]]) 
# a.shape =  (3,2)  
# print (a)                  # 输出 [[1 2] [3 4] [5 6]]
# # NumPy 也提供了 reshape 函数来调整数组大小。
# # 通常返回的是非拷贝副本，即改变返回后数组的元素，原数组对应元素的值也会改变
# a = np.array([[1,2,3],[4,5,6]]) 
# b = a.reshape(3,2)  
# print (b)                  # 输出 [[1 2] [3 4] [5 6]]
# # 还可以使用 resize 函数来调整数组大小。
# a = np.array([[1,2,3],[4,5,6]]) 
# a.resize(3,2)  
# print (a)                  # 输出 [[1 2] [3 4] [5 6]]

# a = np.array([[1,2,3],[4,5,6]]) 
# # a.shape =  (3,2)  
# b = a.reshape(3,2)  
# print (b)
# print (a)
# print (b.dtype)
# print (a.dtype)
# # print (a.size)

x = np.empty([3,2], dtype = int) 
print (x)

x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print ('我们的数组是：' )
print (x)
print ('\n')
rows = np.array([[0,0],[3,3]]) 
cols = np.array([[0,2],[0,2]]) 
print(f'rows= {rows}')
y = x[rows,cols]  
y = x[[0,3],:] [:,[0,2]] 
print  ('这个数组的四个角元素是：')
print (y)
print(f'=========> { x[[1,2],[1]]}')


# a = np.array([[1,2,3], [4,5,6],[7,8,9],[7,8,9]])
# b = a[1:3, 1:3]
# c = a[1:3,[1,2]]
# d = a[...,1:]
# print(f'b= {b}')
# print(f'c= {c}')
# print(f'd= {d}')