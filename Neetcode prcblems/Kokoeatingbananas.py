from typing import List
import math

"""Brute Force"""

# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         speed = 1
#         while True:
#             totalTime = 0
#             for pile in piles:
#                 totalTime += math.ceil(pile / speed)
            
#             if totalTime <= h:
#                 return speed
#             speed += 1
#         return speed

"""Binary Search"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
    
piles = [25,10,23,4]
h = 4
    
s = Solution()

print(s.minEatingSpeed(piles,h))