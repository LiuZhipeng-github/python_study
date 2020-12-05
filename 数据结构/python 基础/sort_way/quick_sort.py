'''
快速排序（重点）：最内层循环给第一个值找对应他的位置，然后以这个位置分成两半，再次分别调用快排函数
时间复杂度为n*log2(n),最坏的情况为O(n^2)，这种情况是每次分一半的时候左边或右边只分出来一个元素！！
'''

def quick_sort(alist, first, last):
    # n = len(alist)
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value

    quick_sort(alist, first, low - 1)
    quick_sort(alist, low + 1, last)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)
