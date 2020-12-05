'''
（重要）在对新节点要对链表进行操作的时候，最大的原则就是要先将新节点的prev与next先连起来，再去操作链表，这样防止链表中断
'''
class Node(object):
    def __init__(self, item):
        self.elem = item
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

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

        :param pos:从0开始
        :param item:
        :return:
        '''
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

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur  # 与单向单链表相比新增的pre

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node
        if node.next:
            node.next.prev = node

    def remove(self, item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是不是头节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None  # 删除头节点的下一个节点的prev要为None！！！
                else:
                    cur.prev.next = cur.next
                    if cur.next:  # 判断是不是尾节点，若是尾节点就不用将将cur.next的prev赋值了因为本身就是空的
                        cur.next.prev = cur.prev
                break
            else:
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
    ll = DoubleLinkList()
    ll.add(1)
    ll.travel()
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
    print(ll.length())
