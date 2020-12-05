'''
选择排序：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。
时间复杂度为O(n^2)但不稳定（考虑升序每次选择最大的情况）
'''


def selection_sort(alist):
    for j in range(0, len(alist) - 1):  # 多次找到每次中最小的数
        min = j
        for i in range(j + 1, len(alist)):
            if alist[min] > alist[i]:  # 先找一遍，找到数字最小的下标，就找到了最小的数
                min = i
        alist[j], alist[min] = alist[min], alist[j]
    print(alist)


alist = [7, 6, 5, 7, 3, 1, 2]
selection_sort(alist)
