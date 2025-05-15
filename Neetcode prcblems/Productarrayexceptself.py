from typing import List

"""My solution"""
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         productres = []
#         for i in range(len(nums)):
#             product = 1
#             print(f'numm:{nums[i]}')
#             for j in range(len(nums)):
#                 print(f'numj:{nums[j]}')
#                 print(f'product:{product}')
#                 if j == i:
#                     print('Itself')
#                     continue
#                 else:
#                     product *= nums[j]
#             productres.append(product)

#         return productres

"""Brute Force solution"""
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         res = [0] * n

#         for i in range(n):
#             prod = 1
#             for j in range(n):
#                 if i == j:
#                     continue    
#                 prod *= nums[j]
            
#             res[i] = prod
#         return res


"""Division solution"""

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         prod, zero_cnt = 1, 0
#         for num in nums:
#             if num:
#                 prod *= num
#             else:
#                 zero_cnt +=  1
#         if zero_cnt > 1: return [0] * len(nums)

#         res = [0] * len(nums)
#         for i, c in enumerate(nums):
#             if zero_cnt: res[i] = 0 if c else prod
#             else: res[i] = prod // c
#         return res
    
"""Prefix & Suffix Solution"""

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         res = [0] * n
#         pref = [0] * n
#         suff = [0] * n

#         pref[0] = suff[n - 1] = 1
#         for i in range(1, n):
#             pref[i] = nums[i - 1] * pref[i - 1]
#         for i in range(n - 2, -1, -1):
#             suff[i] = nums[i + 1] * suff[i + 1]
#         for i in range(n):
#             res[i] = pref[i] * suff[i] 
#         return res
    
"""Prefix & Suffix Optimal Solution"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    
nums = [1,2,4,6]
a = Solution()
print(a.productExceptSelf(nums))