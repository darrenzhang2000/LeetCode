class Solution:
    def minWastedSpace(self, A, boxes):
        A.sort()
        res = float('inf')
        for B in boxes:
            B.sort()
            if B[-1] < A[-1]: continue
            cur = i = 0
            for b in B:
                j = bisect.bisect(A, b, i)
                cur += b * (j - i)
                i = j
            res = min(res, cur)
        return (res - sum(A)) % (10**9 + 7) if res < float('inf') else -1        
        
