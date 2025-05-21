from typing import List
from collections import defaultdict

"""My Solution (two pointers)"""
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         r,l = len(numbers)-1,0

#         while r > l:
#             sum2 = numbers[l]+ numbers[r]

#             if sum2 > target:
#                 r -= 1
#             elif sum2 < target:
#                 l +=1
#             else:
#                 return[l+1,r+1]
#         return []


"""Brute Force Solution"""

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             for j in range(i + 1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     return [i + 1, j + 1]
#         return []



"""Hash Map"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
        return []

"""Binary serach"""

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             l, r = i + 1, len(numbers) - 1
#             tmp = target - numbers[i]
#             while l <= r:
#                 mid = l + (r - l)//2
#                 if numbers[mid] == tmp:
#                     return [i + 1, mid + 1]
#                 elif numbers[mid] < tmp:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#         return []

numbers = [1,2,3,4]
target = 3

a = Solution()
print(a.twoSum(numbers,target))


