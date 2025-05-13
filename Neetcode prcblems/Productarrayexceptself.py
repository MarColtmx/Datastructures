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
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue    
                prod *= nums[j]
            
            res[i] = prod
        return res

nums = [1,2,4,6]
a = Solution()
print(a.productExceptSelf(nums))


