from typing import List

"""My solution"""

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         result = [] #* len(temperatures)
#         print(result)
#         for temp in range(len(temperatures)):
#             count =0
#             print(temp)
#             for d  in range(temp +1,len(temperatures)):
#                 print(f'day{d}')
#                 count+=1
#                 if temperatures[temp]<temperatures[d]:
#                     result.append(count)
#                     break
#                 if d == len(temperatures)-1 and not temperatures[temp]<temperatures[d]:
#                     print(len(temperatures))
#                     result.append(0)
#             if temp == len(temperatures)-1:
#                result.append(0) 
#         return result
    
"""Brute Force Solution"""

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         n = len(temperatures)
#         res = []

#         for i in range(n):
#             count = 1
#             j = i + 1
#             while j < n:
#                 if temperatures[j] > temperatures[i]:
#                     break
#                 j += 1
#                 count += 1
#             count = 0 if j == n else count
#             res.append(count)
#         return res


"""Stack Solution"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

temperatures = [30,38,30,36,35,40,28]
#temperatures = [22,21,20]

s = Solution()
print(s.dailyTemperatures(temperatures))
