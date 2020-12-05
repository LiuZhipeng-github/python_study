# 未优化的插入排序算法的时间复杂度为O(n^2)
# def insert_sort(alist):
#     # 从第二个位置，即下标为1的元素开始向前插入
#     for i in range(1, len(alist)):
#         # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
#         for j in range(i, 0, -1):
#             if alist[j] < alist[j - 1]:
#                 alist[j], alist[j - 1] = alist[j - 1], alist[j]
#
#
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# insert_sort(alist)
# print(alist)


# 优化后的插入排序算法时间复杂度要小于O(n^2),但是最坏的情况还是O(n^2)，最好情况为O(n）
def inseart_sort_amd(alist):
    n = len(alist)
    for j in range(1,n):
        i = j
        while i >0:
            if alist[i] < alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
                i -= 1
            else:
                break

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
inseart_sort_amd(alist)
print(alist)