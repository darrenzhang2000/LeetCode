class Solution:
    def findCelebrity(self, n: int) -> int:
        i = 0
        j = 1
        while True:
            if knows(i, j): # i cannot be cele. j can be cele
                i = max(i + 1, j + 1)
            else:
                j = max(i + 1, j + 1)
            if i == n or j == n:
                break
        candidate = min(i, j)
        for i in range(n):
            if i == candidate:
                continue
            if not knows(i, candidate) or knows(candidate, i):
                return -1
            
        return candidate
