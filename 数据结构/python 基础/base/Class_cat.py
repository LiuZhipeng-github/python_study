"""
封装类cat
"""
class Cat:
    """
    这是一只猫的类
    """
    def __init__(self,name,taillen=10):
        self.name = name
        self.__privatename = name  # 受保护的对象，不能被直接读取或调用

        self.taillen = taillen
        print('我是一只猫，我叫%s' % self.name)
    def __call__(self, *args, **kwargs):
        print("cat:",args[0]+args[1])  # 调用这个类会像函数一样被调用
    def __str__(self): #使这个类可使用print()方法,返回str类型的数据
        re_str = '我是%s' % self.name
        return re_str
    def __len__(self):  #使这个类可使用len()方法
        return self.taillen
    def __iter__(self): #使这个类可迭代
        return iter([1,2,3,4])

    # 可以对应字典的查，改，删
    def __getitem__(self, item):
        if item == 'name':
            return self.name
        else:
            return None
    def __setitem__(self, key, value):
        if key == 'name':
            self.name = value
    def __delitem__(self, key):
        if key == 'name':
            del self.name
    # 还有__sub__、__mul__、__div__、__mod__、__pov__
    def __add__(self, other):
        if isinstance(other,Cat):
            return [self,other]
        elif isinstance(other,list):
            other.append(self)
            return other

    def __del__(self):
        print('我被系统回收了')  # 整个类被调用结束后才会被调用