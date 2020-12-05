'''
二分查找：用这个查找方法的目标序列必须是有序序列！！
'''

def binary_search(alist, item):
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid + 1:], item)
    return False


def _binary_search(alist, item):
    '''非递归版本'''
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (last + first) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(li, 7))
    print(binary_search(li, 10))
    print(_binary_search(li, 5))
    print(_binary_search(li, 11))
