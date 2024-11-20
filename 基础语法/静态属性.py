#Demo:Static Attr
class Manager():
	#静态属性，所有实例只有一个备份，用户实现--单例模型或者资源管理还是有些用处的
    data_set = {}
    access_count = 0
    def __init__(self,num):
        Manager.data_set['default']={
            'name':'init_name',
            'data':[num]
        }
        #成员属性可以与静态属性重名
        self.data_set = "I'm not a static one"
 	#成员方法也可以访问静态属性   
    def show(self):
        print("static:",Manager.getData())
        print("instance:",self.data_set)

    #静态方法只能访问静态属性
    @staticmethod
    def getData():
        Manager.access_count += 1
        return Manager.data_set


if __name__=="__main__":
    #可以直接访问
    print(Manager.data_set)
    #通过静态成员方法访问
    print(Manager.getData())

    #通过实例成员方法访问
    manager = Manager(5)
    Manager.data_set['new key']='a value'
    manager.show()

    #再看一眼静态属性
    print(Manager.getData())
    print("count:",Manager.access_count)
    #实例化的对象属性
    print(manager.__dict__)

