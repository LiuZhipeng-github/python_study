import collections

'''
第一次test
'''

# def test(dict):
#     dict2 = {'f': 1, 'g': 2, 'h': '3'}
#     dict.update(dict2)  # 即使没有返回值也能将更新字典
#
#
# def main():
#     dict3 = {}
#     dict = {'a': 1, 'b': 2, 'b': '3'}
#     print(dict3)
#     test(dict3)
#     print(dict3)


'''
第二次
'''

# def test2():
#     return False
# print(test2(),'------------')
# if test2() is True:
#     print('failed')
# name_tuple = collections.namedtuple('parent','name,age,sex,id')
# nt = name_tuple(name='Alaex',age=20,sex='F',id=90909090)
# print(nt[0],nt[2],nt[1],nt[3])

'''
第三次
'''
# print('000000',end=' ')
# print()
# print('1111111')
# if __name__ == '__main__':
#     main()
'''
第四次
'''

# for i in range(1,8):
#     print(i)
'''
第五次
'''

#
# def reverseVowels(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     s = list(s)
#     n = len(s)
#
#     yuan = ['a', 'i', 'o', 'u', 'e']
#     left = 0
#     right = n - 1
#     while left < right:
#         if s[left] in yuan:
#             if s[right] in yuan:
#                 s[left], s[right] = s[right], s[left]
#                 right -= 1
#                 left += 1
#             else:
#                 right -= 1
#         else:
#             left += 1
#
#     return ''.join(s)
'''
第六次:相邻花园上不同色问题
'''

# def gardenNoAdj(N, paths):
#     """
#     :type N: int
#     :type paths: List[List[int]]
#     :rtype: List[int]
#     """
#     if paths == []:
#         return [1] * N
#     r = [0] * N
#     G = [[] for i in range(N)]
#     for x, y in paths:
#        G[x - 1].append(y - 1)
#        G[y - 1].append(x - 1)
#     print(G)
#     for i in range(N):
#         r[i] = ({1, 2, 3, 4} - {r[j] for j in G[i]}).pop()
#
#     return r
'''
回溯算法
'''
# def back(i,n):
#     print(i)
#     for j in range(i,n):
#         back(j+1,n)
#
# back(0,3)



'''
滑动窗口
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_num = 0
        length = len(s)
        for i in range(length):
            aft = i+1
            tem = []
            while True:
                if aft >= length:
                    max_num = max(max_num,len(s[i:aft]))
                    break
                if s[i] == s[aft]:
                    max_num = max(max_num,len(s[i:aft]))
                    break
                if s[aft] in tem:
                    max_num = max(max_num,len(s[i:aft]))
                    break
                tem.append(s[aft])
                aft += 1
        return max_num
# if __name__ == '__main__':