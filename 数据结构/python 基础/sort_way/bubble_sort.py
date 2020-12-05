'''
冒泡排序算法
原理：
比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
时间复杂度为O(n^2)，最优时为O(n)且稳定
'''

def bubble_sort(alist):
    for j in range(len(alist) - 1):
        for i in range(len(alist) - 1 - j):
            count = 0
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if count == 0:  # 如果最优时间复杂度时，内层循环走了一遍发现不需要排序，直接就退出外层循环，所以最优时间复杂度为O(n)
            return
    print(alist)


alist = [7, 6, 5, 7, 3, 1, 2]
bubble_sort(alist)
