from typing import List
ums = [5,6,1,8,3,9,5]
target = 10

"""My solution"""
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(1, len(nums)):
#                 if nums[i]+nums[j] == 10:
#                     return [i,j]

"""Sort Solution"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        
        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]), 
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []

"""Hash Map Solution two pass"""  

# class Solution:
#     """
#     A class to solve the Two Sum problem.
#     Methods
#     -------
#     twoSum(nums: List[int], target: int) -> List[int]:
#         Finds two indices in the list `nums` such that the numbers at those
#         indices add up to the `target`.
#     """
#     """
#     Finds two indices in the list `nums` such that the numbers at those
#     indices add up to the `target`.
#     Parameters
#     ----------
#     nums : List[int]
#         A list of integers.
#     target : int
#         The target sum to find.
#     Returns
#     -------
#     List[int]
#         A list containing two indices of the numbers in `nums` that add up
#         to the `target`. If no such indices exist, the behavior is undefined.
#     Notes
#     -----
#     - Assumes there is exactly one solution, and each input would have
#         exactly one solution.
#     - The same element cannot be used twice.
#     """
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         indices = {}  # val -> index

#         for i, n in enumerate(nums):
#             indices[n] = i

#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in indices and indices[diff] != i:
#                 return [i, indices[diff]]
"""Hash Map Solution one pass"""  
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

def twoSum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i


print(twoSum(ums,target))
a = Solution()
print(a.twoSum(ums,target))