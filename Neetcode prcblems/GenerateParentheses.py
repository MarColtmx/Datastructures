from typing import List

"""Brute Force Solutiom"""
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []

#         def valid(s: str):
#             open = 0
#             for c in s:
#                 open += 1 if c == '(' else -1
#                 if open < 0:
#                     return False
#             return not open

#         def dfs(s: str):
#             if n * 2 == len(s):
#                 if valid(s):
#                     res.append(s)
#                 return
            
#             dfs(s + '(')
#             dfs(s + ')')
        
#         dfs("")
#         return res

"""Backtracking Solution"""

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         stack = []
#         res = []

#         def backtrack(openN, closedN):
#             if openN == closedN == n:
#                 res.append("".join(stack))
#                 return

#             if openN < n:
#                 stack.append("(")
#                 backtrack(openN + 1, closedN)
#                 stack.pop()
#             if closedN < openN:
#                 stack.append(")")
#                 backtrack(openN, closedN + 1)
#                 stack.pop()

#         backtrack(0, 0)
#         return res

"""Dynamic Programming"""

class Solution:
    def generateParenthesis(self, n):
        res = [[] for _ in range(n+1)]
        res[0] = [""]
        
        for k in range(n + 1):
            for i in range(k):
                for left in res[i]:
                    for right in res[k-i-1]:
                        res[k].append("(" + left + ")" + right)
        
        return res[-1]

n=3

s = Solution()
print(s.generateParenthesis(n))