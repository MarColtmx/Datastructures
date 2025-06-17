from typing import List

"""My solution"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, (len(nums)-1)

        while l <= r:
            i = (l+r)//2

            if target == nums[i]:
                return i
            if nums[l] <= nums[i]:
                if target > nums[i] or target < nums[l]:
                    l = i+1
                else :
                    r = i-1

            else:
                if target > nums[r] or target < nums[i]:
                    r = i -1
                else:
                    l = i+1
        return -1

nums = [3,4,5,6,1,2]
target = 7

s = Solution()
print(s.search(nums,target))