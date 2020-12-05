class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        # print(self.root)
        if self.root == None:
            self.root = node  # 第一遍赋值根节点
            return
        queue = [self.root]  # 这个列表只用来放置每一层的根节点，然后对处理一个删掉一个，添加完成后退出
        while queue:  # 直到这个了根节点列表为空，说明最下面一层根节点再无子节点
            cur_node = queue.pop(0)   # 删除最外层根节点并赋值，进行处理
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        '''层次遍历'''
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def pre_order(self, node):
        '''先序遍历：根节点>左子树>右子树'''
        if node is None:
            return
        print(node.elem, end=' ')
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def in_order(self, node):
        '''中序遍历：左子树>根节点>右子树'''
        if node is None:
            return
        self.in_order(node.lchild)
        print(node.elem, end=' ')
        self.in_order(node.rchild)

    def after_order(self, node):
        '''后序遍历：左子树>右子树>根节点'''
        if node is None:
            return
        self.after_order(node.lchild)
        self.after_order(node.rchild)
        print(node.elem, end=' ')


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print('')
    tree.pre_order(tree.root)
    print('')
    tree.after_order(tree.root)
    print('')
    tree.in_order(tree.root)

