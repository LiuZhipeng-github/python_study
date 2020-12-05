'''
数据结构之双端队列：两端都可进可出
Deque() 创建一个空的双端队列
add_front(item) 从队头加入一个item元素
add_rear(item) 从队尾加入一个item元素
remove_front() 从队头删除一个item元素
remove_rear() 从队尾删除一个item元素
is_empty() 判断双端队列是否为空
size() 返回队列的大小
'''


class Deque(object):
    """双端队列"""

    def __init__(self):
        self.__items = []

    def is_empty(self):
        """判断队列是否为空"""
        return self.__items == []

    def add_front(self, item):
        """在队头添加元素"""
        self.__items.insert(0, item)

    def add_rear(self, item):
        """在队尾添加元素"""
        self.__items.append(item)

    def remove_front(self):
        """从队头删除元素"""
        return self.__items.pop(0)

    def remove_rear(self):
        """从队尾删除元素"""
        return self.__items.pop()

    def size(self):
        """返回队列大小"""
        return len(self.__items)


# 头尾都可以插入和删除
if __name__ == "__main__":
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    deque.add_rear(4)
    print(deque.size())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_rear())
    print(deque.remove_rear())
