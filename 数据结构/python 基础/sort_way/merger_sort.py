'''
归并排序算法：把序列分成一个一个的，然后两两排序，之后向上一对一对排序，四个四个排序，应用快速排序原理(左右游标)将符合条件的数放入新的列表
思路：将数组分解最小之后，然后合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。
典型的牺牲空间换取时间的排序方法
时间复杂度为n*log2(n)且稳定
'''


def merage_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    # 返回的应该是有序的序列
    left = merage_sort(alist[:mid])
    right = merage_sort(alist[mid:])

    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result += left[left_pointer:]
    result += right[right_pointer:]
    return result


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sort_list = merage_sort(alist)
    print(alist)
    print(sort_list)
