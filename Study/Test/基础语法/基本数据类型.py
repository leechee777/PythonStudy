# Python3 中常见的数据类型有：

# Number（数字）
# String（字符串）
# bool（布尔类型）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）
# Python3 的六个标准数据类型中：

# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
# 此外还有一些高级的数据类型，如: 字节数组类型(bytes)。
# ------------------------------------------------------------
# python中数字有四种类型：整数、布尔型、浮点数和复数。

# int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# bool (布尔), 如 True。
# float (浮点数), 如 1.23、3E-2
# complex (复数) - 复数由实部和虚部组成，形式为 a + bj，其中 a 是实部，b 是虚部，j 表示虚数单位。如 1 + 2j、 1.1 + 2.2j
# ------------------------------------------------------------
import time


print('Number------------------------------------------------------------')
a = True
print(int(a))
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int)) # 判断a是否为整数
# ------------------------------------------------------------
# isinstance 和 type 的区别在于：

# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
# Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
# ------------------------------------------------------------
print('Bool------------------------------------------------------------')
print(issubclass(bool, int) )
print(True==1)
print(False==0)
print(True+1)
print(False+1)
print(1 is True)
print(0 is False)
# ------------------------------------------------------------
print('Tuple------------------------------------------------------------')
tup1 = tuple()   # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
print(bool(tup1))

# ------------------------------------------------------------
print('Set------------------------------------------------------------')
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Google'}
print(sites)   # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

# ------------------------------------------------------------
print('Dictionary------------------------------------------------------------')
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

# ------------------------------------------------------------
print('bytes ------------------------------------------------------------')
x = bytes("hello", encoding="utf-8")
print(x)
x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"

x = b"hello"
print(x[0])
if x[0] == ord("h"):  #其中 ord() 函数用于将字符转换为相应的整数值。
    print("The first element is 'h'")

# ------------------------------------------------------------

var1 = 'Hello World!' 
print ("已更新字符串 : ", var1[:6] + 'Runoob!')

# 使用 \r 实现百分比进度：
for i in range(101):
    print("\r{:3}%".format(i),end=' ')
    time.sleep(0.05)