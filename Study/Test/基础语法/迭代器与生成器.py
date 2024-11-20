# #!/usr/bin/python3
 
# import sys         # 引入 sys 模块
# print('迭代器 ------------------------------------------------------------')
 
# # list=[1,2,3,4]
# # it = iter(list)    # 创建迭代器对象
 
# # while True:
# #     try:
# #         print (next(it))
# #     except StopIteration:
# #         sys.exit()

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
 
#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration
 
# myclass = MyNumbers()
# # myiter = iter(myclass)
 
# for x in myclass:
#   print(x)


# print('生成器 ------------------------------------------------------------')

# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
 
# # 创建生成器对象
# generator = countdown(5)
 
# # 通过迭代生成器获取值
# print(next(generator))  # 输出: 5
# print(next(generator))  # 输出: 4
# print(next(generator))  # 输出: 3
 
# # 使用 for 循环迭代生成器
# for value in generator:
#     print(value)  # 输出: 2 1

class creatEven:
    def __init__(self, min, max):
        self.value = min
        self.min = min
        self.max = max

 
    def __iter__(self):
        print('__iter__')
        return self
    def __next__(self):
        print('__next__')
        self.value += 2
        return self.value
    
myEvneList = creatEven(0, 6)
for i in myEvneList:
    print(i)
    if(i>=10):
        break