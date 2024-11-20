import numpy as np
# x =  np.arange(35).reshape(5, 7)
# print(x)
# y = x[[0, 1, 2], [0, 1, 0]]
# print(y)

# x = np.linspace(2.0, 3.0, num=5, endpoint=False)
# x = np.random.randn(6, 4)
# x = np.random.randint(3,7,size=(2, 4))
# x = np.array( [10,20,30,40] )[1:3:2]  # 切片(从0开始计算),起始位置1，终止位置3(不包含)，步长为2
# print(x)

a = np.array( [10,20,30,40] )
b = np.array( [1, 2, 3, 4] )
# x = 4*np.sin(a)
# x = a.max() # 40
# x = a.min() # 10
# x = a.sum() # 100
# x = a.std() # 11.180339887498949
# x = a.all() # True
# x = a.cumsum() # array([ 10,  30,  60, 100])
# x = b.sum(axis=1) # 多维可以指定方向
# np.negative(-1) # 1 相反数
# print(x)

x = 10
# y = np.where(False, 1, 10) # array(1)
y = np.logical_and(x>0, x>5) # True
# y = np.logical_or(x>0, x<5) # True
# y = np.logical_not(x>5) # False
# y = np.logical_xor(x>5, x==0) # 异或 True
print(y)