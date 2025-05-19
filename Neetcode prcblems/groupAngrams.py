from typing import List
from collections import defaultdict
strs = ["act","pots","tops","cat","stop","hat"]

"""Sorted Solution"""

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             sortedS = ''.join(sorted(s))
#             res[sortedS].append(s)
#         return list(res.values())

"""Hash map Solution"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                print(count)
            res[tuple(count)].append(s)
        return list(res.values())
    
a = Solution()
print(a.groupAnagrams(strs))