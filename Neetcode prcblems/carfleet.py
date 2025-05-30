from typing import List

"""My solution"""
# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         time = []
#         pair = [(p, s) for p, s in zip(position, speed)]
#         pair.sort(reverse=True)
#         print(pair)
#         fletcount= 1

#         for j,i in enumerate(pair):
#             t = (target-i[0])/i[1]
#             if t in time:
#                 continue
#             else:
#                 time.append(t)
#             if len(time) > 1:
#                 time.sort(reverse=True)
#                 if time[1] >= t:
#                     continue
                
#                 else:
#                     fletcount += 1
#         return fletcount

"""Stack Solution"""
# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         pair = [(p, s) for p, s in zip(position, speed)]
#         pair.sort(reverse=True)
#         print(pair)
#         stack = []
#         for p, s in pair:  # Reverse Sorted Order
#             stack.append((target - p) / s)
#             if len(stack) >= 2 and stack[-1] <= stack[-2]:
#                 stack.pop()
#         return len(stack)
    

"""Iteration solution"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            currCar = pair[i]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets

target=12
position=[10,8,0,5,3]
speed=[2,4,1,1,3]

# target = 10
# position = [4,1,0,7]
# speed = [2,2,1,1]

s =Solution()
print(s.carFleet(target,position,speed))
