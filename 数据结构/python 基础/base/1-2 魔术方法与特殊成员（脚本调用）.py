"""
脚本调用类Cat
"""
from Class_cat import Cat
#__init__
cat = Cat('Tom',16)  # 实例化Cat类

#__doc____module__ __class__
# print(cat.__doc__)
# print(cat.__module__)
# print(cat.__class__)

# __call__
"""
def fun(a,b):
    print(a+b)
fun(1,2)
"""
cat(1,2)#与函数调用类似
print(callable(cat))


# __dict__
print(cat.__dict__)
print(cat._Cat__privatename)
print(cat.name)

#__str__
print(str(cat))
print(cat)


#__len__
print(len(cat))
cat_2 = Cat('jack',17)
print(len(cat_2))

#__iter__
for i in cat:
    print(i)

#__grtitem__ __setitem__ __delitem__
#正常字典操作——查、改、删
dic = {'name':'Tom','age':7,'dep':'ccb'}
print(dic['name'])
dic['name'] = 'jack'
del dic['age']
print(dic)

print(cat['name'])
cat["name"] = 'jim'
print(cat['name'])
# del cat['name']
# print(cat.name)

#数学运算+—__add__
cat1 = Cat('black',28)
cat2 = Cat('whiet',3)
print(cat1+cat2)

cats = cat1+cat2
cat3 = Cat('Alen')
# print(cats+cat3)
cat