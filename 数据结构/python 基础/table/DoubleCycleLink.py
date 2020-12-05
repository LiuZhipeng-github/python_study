'''
双向循环列表
'''


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


class DoubleCycleLink(object):

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        """返回链表的长度"""
        # 如果链表为空，返回长度0
        if self.is_empty():
            return 0
        count = 1
        cur = self.__head
        while cur.next != self.__head:  # 只要下一个节点不再是头节点就可以继续遍历
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return False
        cur = self.__head
        print(cur.elem, end=' ')
        while cur.next != self.__head:
            cur = cur.next
            print(cur.elem, end=' ')
        print()

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            self.__head.next = node
            self.__head.prev = node
        else:
            # 添加的节点指向_head
            node.next = self.__head
            node.prev = self.__head.prev
            self.__head.prev.next = node
            self.__head.prev = node
            # cur = self.__head
            # while cur.next!=self.__head:
            #     cur.next
            # cur.next = node
            self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head  # 如果为空链表不仅要将node赋值为头节点还要循环指向自己
            node.prev = self.__head
        else:
            # 移到链表尾部
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.prev = cur
            node.next = self.__head
            # 将尾节点指向node
            cur.next = node
            self.__head.prev = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            cur = self.__head  # 把初始位置的节点指向cur
            count = 0
            while count < pos:  # 游标的位置就是目标位置！！！
                count += 1
                cur = cur.next  # 当循环结束后，cur指向pos的位置
            node = Node(item)
            node.next = cur  # 将这个新插入的节点的后节点指向现在在目标位置的节点
            node.prev = cur.prev  # 将这个新插入的节点的后节点指向现在在目标位置的节点的前一个节点
            cur.prev.next = node  # 目标位置的前一个节点的下一个节点替换为node
            cur.prev = node  # 被后移的这个节点的前一个节点是新的node

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        if cur.elem == item:
            return True
        while cur.next != self.__head:
            cur = cur.next
            if cur.elem == item:
                return True
        return False

    def remove(self, item):
        """删除一个节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
            # 将cur指向头节点
        cur = self.__head
        # 若头节点的元素就是要查找的元素item
        if cur.elem == item:
            # 如果链表不止一个节点
            if cur.next != self.__head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while cur.next != self.__head:
                    cur = cur.next
                    # cur指向了尾节点
                cur.next = self.__head.next  # 尾节点的下一个节点为头节点的下一个节点
                self.__head.next.prev = self.__head.next
                self.__head = self.__head.next  # 新的头节点是原头节点的下一个节点

            else:
                # 链表只有一个节点
                self.__head = None
        else:

            # 第一个节点不是要删除的
            while cur.next != self.__head:
                # 找到了要删除的元素
                if cur.elem == item:
                    # 删除
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    return
                else:

                    cur = cur.next
                    # cur 指向尾节点
            if cur.elem == item:  # 因为尾节点的下一个节点是头节点，所以上面的while循环没有进去，所以要额外添加一个判断
                # 尾部删除
                cur.prev.next = cur.next
                cur.next.prev = cur.prev

    def back_travel(self):
        if self.is_empty():
            return False
        cur = self.__head
        print(cur.elem, end=' ')
        while cur.prev != self.__head:
            cur = cur.prev
            print(cur.elem, end=' ')
        print()


if __name__ == '__main__':
    ll = DoubleCycleLink()
    # ll.add(1)
    # ll.travel()
    # ll.add(2)
    # ll.add(3)
    # ll.add(4)
    # ll.add(5)
    # ll.travel()
    # print(ll.length())
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.add(7)
    ll.add(8)
    ll.add(9)
    ll.add(10)
    # ll.travel()
    # ll.insert(2,8)
    # ll.travel()
    # print(ll.search(0))
    # ll.remove(3)
    # ll.travel()
    # ll.remove(1)
    # ll.travel()
    # ll.append(9)
    # ll.add(1)
    # ll.travel()
    # ll.remove(8)
    # ll.travel()
    ll.back_travel()
