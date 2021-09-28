class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def findPrevEndProf(memo, st):
            i = bisect.bisect(memo, Info(st + 1, float('-inf'))) - 1
            return memo[i]
            # for i in range(len(memo)-1, -1, -1):
            #     if memo[i].end <= st:
            #         return memo[i]
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[1])
        Info = namedtuple('Info', ('end', 'profit'))
        memo = [Info(0, 0)]
        for st, et, prof in jobs:
            prevMax = memo[-1]
            
            prevEndProf = findPrevEndProf(memo, st)
            withCur = Info(et, prof + prevEndProf.profit)
            info = withCur if withCur.profit > prevMax.profit else prevMax
            memo.append(info)
        return memo[-1].profit
        
