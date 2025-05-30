s = "racecar"
t = "carrace"
# sorted solution
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         return sorted(s) == sorted(t)

# a = Solution()
# print(a.isAnagram(s,t))

# from collections import Counter

# def isAnagram(s: str, t: str) -> bool:
#     return Counter(s) == Counter(t)

# print(isAnagram(s,t))
"""Hash Table solution"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True

"""Hash Map solution"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

a = Solution()
print(a.isAnagram(s,t))
