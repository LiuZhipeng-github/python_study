'''
希尔排序:在插入排序的基础上加入了布长gap
时间复杂度为O(n^2)且不稳定
'''


def shell_sort(alist):
    # 从第二个位置，即下标为1的元素开始向前插入
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
            while j >= gap and alist[j - gap] > alist[j]:
                alist[j - gap], alist[j] = alist[j], alist[j - gap]
                j -= gap
                # 得到新的步长
        gap = gap // 2
    return alist


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
alist = shell_sort(alist)
print(alist)
