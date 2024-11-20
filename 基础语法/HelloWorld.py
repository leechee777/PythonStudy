#!/usr/bin/python3
# ------------------------------------------------------------
# str='123456789'
# print(str)                 # 输出字符串
# print(str[0:])           # 输出第一个到倒数第二个的所有字符
# print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
# print(str[::-1])           # 输出字符串反转后的结果
# print(str[1:5])           # 输出从第二个到第五个的字符
# print(str[1:])           # 输出从第二个到最后的字符
# print(str*2)               # 输出字符串两次
# print(str+'你好')           # 连接字符串
# print(r'hello\nworld')      # 使用反斜杠(\)转义特殊字符
# print(f'hello\tworld')      # 使用反斜杠(\)转义特殊字符
# ------------------------------------------------------------
# input("\n\n按下 enter 键后退出。")
# ------------------------------------------------------------
# import sys; x = 'runoob'; sys.stdout.write(x + '\n')
# import sys
# sys.stdout.write(" hi ")    # hi 前后各有 1 个空格
# ------------------------------------------------------------
# x="a"
# y="b"
# # 换行输出
# print( x )
# print( y )
 
# print('---------')
# # 不换行输出
# print( x, end=" " )
# print( y, end="hhh" )
# print()
# ------------------------------------------------------------
# import sys
# print('================Python import mode==========================')
# print ('命令行参数为:')
# for i in sys.argv:
#     print (i)
# print ('\n python 路径为',sys.path)

from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
for i in path:
    print (i)
# print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path