class Node(object):
    """节点"""

    def __init__(self, item):
        self.item = item
        self.next = None


class SinCycLinkedlist(object):
    """单向循环链表"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """返回链表的长度"""
        # 如果链表为空，返回长度0
        if self.is_empty():
            return 0
        count = 1
        cur = self._head
        while cur.next != self._head:  # 只要下一个节点不再是头节点就可以继续遍历
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self._head
        print(cur.item, end=' ')
        while cur.next != self._head:
            cur = cur.next
            print(cur.item, end=' ')
        print("")

    def add(self, item):
        """头部添加节点：先将node的next指向头节点，再从头节点遍历到最后，将最后的节点的next指向node，最后将node做为头节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            # 添加的节点指向_head
            node.next = self._head
            # 移到链表尾部，将尾部节点的next指向node
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            # _head指向添加node的
            self._head = node

    def append(self, item):
        """尾部添加节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head  # 如果为空链表不仅要将node赋值为头节点还要循环指向自己
        else:
            # 移到链表尾部
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            # 将尾节点指向node
            cur.next = node
            # 将node指向头节点_head
            node.next = self._head

    def insert(self, pos, item):
        """在指定位置添加节点：这个与单链表一样"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos - 1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除一个节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        # 将cur指向头节点
        cur = self._head
        pre = None
        # 若头节点的元素就是要查找的元素item
        if cur.item == item:
            # 如果链表不止一个节点
            if cur.next != self._head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while cur.next != self._head:
                    cur = cur.next
                # cur指向了尾节点
                cur.next = self._head.next  # 尾节点的下一个节点为头节点的下一个节点
                self._head = self._head.next  # 新的头节点是原头节点的下一个节点
            else:
                # 链表只有一个节点
                self._head = None
        else:
            pre = self._head
            # 第一个节点不是要删除的
            while cur.next != self._head:
                # 找到了要删除的元素
                if cur.item == item:
                    # 删除
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            # cur 指向尾节点
            if cur.item == item:  # 因为尾节点的下一个节点是头节点，所以上面的while循环没有进去，所以要额外添加一个判断
                # 尾部删除
                pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self._head
        if cur.item == item:
            return True
        while cur.next != self._head:  # 这个循环内部是不包含头节点和尾节点的，所以头节点和尾节点都要单独拿出来判断
            cur = cur.next
            if cur.item == item:
                return True
        return False


if __name__ == "__main__":
    ll = SinCycLinkedlist()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.travel()
    # ll.append(3)
    # ll.insert(2, 4)
    # ll.insert(4, 5)
    # ll.insert(0, 6)
    # print("length:", ll.length())
    # ll.travel()
    # print(ll.search(3))
    # print(ll.search(7))
    # ll.remove(1)
    # print("length:", ll.length())
    # ll.travel()
