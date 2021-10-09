class Solution:
    def minDeletions(self, s: str) -> int:
        freqs = Counter(s)
        numDeletions = 0
        curFreq = float('inf')
        for freq in sorted(freqs.values(), reverse=True):
            if curFreq == 0:
                numDeletions += freq
            elif freq < curFreq:
                curFreq = freq
            else:
                numDeletions += freq - curFreq + 1
                curFreq -= 1
        return numDeletions
