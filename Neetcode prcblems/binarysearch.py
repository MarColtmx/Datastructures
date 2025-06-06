from typing import List

"""My solution"""

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         start = 0
#         end = len(nums)-1

#         while start < end:
#             mid = start + end //2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 start +=1
#             else:
#                 end -= 1
#         return -1

"""Recusive Binary search Solutiom"""

# class Solution:
#     def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
#         if l > r:
#             return -1
#         m = l + (r - l) // 2
        
#         if nums[m] == target:
#             return m
#         if nums[m] < target:
#             return self.binary_search(m + 1, r, nums, target)
#         return self.binary_search(l, m - 1, nums, target)

#     def search(self, nums: List[int], target: int) -> int:
#         return self.binary_search(0, len(nums) - 1, nums, target)

"""Iterative Binary Search Solution"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)  

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

nums = [-1,0,2,4,6,8]
target = 4

"""Upper Bund Solution"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)  
            if nums[m] > target:
                r = m
            elif nums[m] <= target:
                l = m + 1
        return l - 1 if (l and nums[l - 1] == target) else -1

s = Solution()
print(s.search(nums,target))