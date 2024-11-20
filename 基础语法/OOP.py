from json import tool


class FileHandle(object): #处理文件的类
    def read(self, path):
        print("read file")
        # 读取文件内容
    def write(self, path, value):
        __path = path
        print("write file")
        # 写入文件内容
class DbHandle(object): #处理数据库的类\
    def read(self, path):
        print("read Db")
        # 读取文件内容
    def write(self, path, value):
        __path = path
        print("write Db")
        # 写入文件内容

#Tool 同时集成了两个类,选择第一个父类
class Tool(DbHandle, FileHandle):
# class Tool(FileHandle, DbHandle):
    def businessLogic(self):
        print("In Tool class")
tool = Tool()
tool.read("C:\\1.txt")

#组合方式实现多继承
# class Tool(object):
#     def __init__(self):
#         self.fileHandle = FileHandle()
#         self.dbHandle = DbHandle()
#     def calDAtaInFile(self, path):
#         self.fileHandle.read(path)
#         #统计文件里的数据

#     def calDataInDb(self, path):
#         self.dbHandle.read(path)
#         #统计数据库里的数据
# tool = Tool()
# tool.calDAtaInFile("C:\\1.txt")
# tool.calDataInDb("C:\\2.db")


print("end".index("d"))
print(["e", "n", "d"].index("d"))
