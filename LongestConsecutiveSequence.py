from typing import List

"""Brute Force"""
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         res = 0
#         store = set(nums)

#         for num in nums:
#             streak, curr = 0, num
#             while curr in store:
#                 streak += 1
#                 curr += 1
#             res = max(res, streak)
#         return res

"""Sorting Solution"""

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         res = 0
#         nums.sort()
        
#         curr, streak = nums[0], 0
#         i = 0
#         while i < len(nums):
#             if curr != nums[i]:
#                 curr = nums[i]
#                 streak = 0
#             while i < len(nums) and nums[i] == curr:
#                 i += 1
#             streak += 1
#             curr += 1
#             res = max(res, streak)
#         return res

"""Hash set"""





nums = [2,20,4,10,3,4,5]
a = Solution()

print(a.longestConsecutive(nums))