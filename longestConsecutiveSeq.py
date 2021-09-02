class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numsSet = {num:False for num in nums}
        maxCount = 0
        for i in range(len(nums)):
            n = nums[i]
            if numsSet[n]:
                continue
            count = 1
            numsSet[n] = True
            sm, lg = nums[i] - 1, nums[i] + 1
            while sm in numsSet:
                numsSet[sm] = True
                sm -= 1
                count += 1
            while lg in numsSet:
                numsSet[lg] = True
                lg += 1
                count += 1
            maxCount = max(maxCount, count)
        print(numsSet)
        return maxCount
