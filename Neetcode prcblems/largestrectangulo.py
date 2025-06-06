from typing import List

"""Brute Force Solution"""

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)
#         maxArea = 0

#         for i in range(n):
#             height = heights[i]

#             rightMost = i + 1
#             while rightMost < n and heights[rightMost] >= height:
#                 rightMost += 1
            
#             leftMost = i
#             while leftMost >= 0 and heights[leftMost] >= height:
#                 leftMost -= 1
            
#             rightMost -= 1
#             leftMost += 1
#             maxArea = max(maxArea, height * (rightMost - leftMost + 1))
#         return maxArea

"""Stack Solution"""

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)
#         stack = []

#         leftMost = [-1] * n
#         print(leftMost)
#         for i in range(n):
#             while stack and heights[stack[-1]] >= heights[i]:
#                 stack.pop()
#             if stack:
#                 leftMost[i] = stack[-1]
#             stack.append(i)
        
#         stack = []
#         rightMost = [n] * n
#         for i in range(n - 1, -1, -1):
#             while stack and heights[stack[-1]] >= heights[i]:
#                 stack.pop()
#             if stack:
#                 rightMost[i] = stack[-1]
#             stack.append(i)
        
#         maxArea = 0
#         for i in range(n):
#             leftMost[i] += 1
#             rightMost[i] -= 1
#             maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
#         return maxArea
    
"""Stack (One pass solution """

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         maxArea = 0
#         stack = []  # pair: (index, height)

#         for i, h in enumerate(heights):
#             start = i
#             while stack and stack[-1][1] > h:
#                 index, height = stack.pop()
#                 maxArea = max(maxArea, height * (i - index))
#                 start = index
#             stack.append((start, h))

#         for i, h in stack:
#             maxArea = max(maxArea, h * (len(heights) - i))
#         return maxArea

"""Stack (Optimal) Solution"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea

heights = [7,1,7,2,2,4]

s = Solution()
print(s.largestRectangleArea(heights))
