from collections import Counter
from typing import List
import heapq

"""My solution"""
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         con = Counter(nums)
#         #Clave = Frequencia 
#         #Valor = Valor numerico o elemento de la lista
#         ordenado = [(valor, clave) for clave, valor in con.most_common()]
#         print(ordenado)
#         return [ordenado[i][1] for i in range(k)]
        

"""Sorting solution"""

# class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = {}
    #     for num in nums:
    #         count[num] = 1 + count.get(num, 0)

    #     arr = []
    #     for num, cnt in count.items():
    #         arr.append([cnt, num])
    #     arr.sort()

    #     print(arr)
    #     res = []
    #     while len(res) < k:
    #         res.append(arr.pop()[1])
    #         print(arr)
    #     return res
    
"""Min-Heap Solution"""

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         for num in nums:
#             count[num] = 1 + count.get(num, 0)

#         heap = []
#         for num in count.keys():
#             heapq.heappush(heap, (count[num], num))
#             if len(heap) > k:
#                 heapq.heappop(heap)

#         res = []
#         for i in range(k):
#             res.append(heapq.heappop(heap)[1])
#         return res

"""Bucket Sort Solution"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

nums = [1,2,2,2,3,3,3]
k = 2

# nums = [7,7]
# k = 1

a = Solution()
print(a.topKFrequent(nums,k))