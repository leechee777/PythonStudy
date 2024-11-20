# # 可写函数说明
# def printinfo( arg1, *vartuple ):
#    "打印任何传入的参数"
#    print ("输出: ")
#    print (arg1)
#    print (vartuple)
 
# # 调用printinfo 函数
# printinfo( 70, 60, 50 )

#!/usr/bin/python3
 
# def outer():
#     num = 10
#     def inner():
#         # nonlocal num   # nonlocal关键字声明
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()

x = False
y = False
z = True

if x or y and z:
    print("yes")
else:
    print("no")