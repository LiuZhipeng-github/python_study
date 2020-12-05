'''
self.next代表的是下一个节点并不是游标！！！！
'''
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None  # 判断self.__head是否为None

    def length(self):
        cur = self.__head
        count = 0
        # cur游标用来移动遍历节点
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print()

    def insert(self, pos, item):
        '''
        比如插到5，那就要找到4的位置，然后将node的pre和node的next都赋上值
        :param pos:从0开始
        :param item:
        :return:
        '''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head  # 把初始位置的节点指向pre
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next  # 当循环结束后，pre指向pos-1的位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def add(self, item):
        '''头加，先将原先的self .__head作为node的next然后重新赋值self.__head'''
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def remove(self, item):
        '''加入辅助游标pre，当找到目标节点时，前一个的next等于后一个游标'''
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是不是头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    ll = SingleLinkList()
    ll.add(1)
    ll.append(6)
    ll.append(0)

    ll.append(4)
    print(ll.is_empty())
    print(ll.length())
    ll.insert(-1, 20)
    ll.insert(2, 100)
    ll.insert(7, 99)
    ll.add(1)
    ll.travel()
    ll.remove(1)
    ll.travel()
    ll.remove(99)
    print(ll.is_empty())
    ll.travel()
