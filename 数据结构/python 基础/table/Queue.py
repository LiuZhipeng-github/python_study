'''
数据结构之队列：先入先出，一端进一端出
Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
'''


class Queue(object):
    """队列"""

    def __init__(self):
        self.__items = []
        # 利用顺序表
    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """进队列"""
        # 方法一：出队列次数多就用法一，因为运算量少
        self.__items.insert(0, item)
        #方法二：入队列次数多就用法二
        # self.__items.append(item)

    def dequeue(self):
        """出队列"""
        return self.__items.pop()
        #方法二
        # return self.__items.pop(0)

    def size(self):
        """返回大小"""
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
