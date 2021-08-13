class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().replace("-", "")[::-1]
        return '-'.join(s[i:i + k] for i in range(0, len(s), k))[::-1]
        
#         w = [c.upper() for c in s if c != '-']
#         if not len(w):
#             return ""
#         res = []
#         count = 0
#         for i in reversed(range(len(w))):
#             res.append(w[i])
#             count += 1
#             if count % k == 0:
#                 res.append('-')
#         if res[-1] == "-":
#             res.pop()
#         return "".join(res)[::-1]
                
