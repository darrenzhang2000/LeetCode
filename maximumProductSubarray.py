class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        max_so_far = [n for n in nums]
        min_so_far = [n for n in nums]
        for i in range(1, len(nums)):
            v = nums[i]
            max_so_far[i] = max(max_so_far[i - 1] * v, v, min_so_far[i - 1] * v)
            min_so_far[i] = min(max_so_far[i - 1] * v, v, min_so_far[i - 1] * v)
            res = max(res, max_so_far[i])
        print(max_so_far, min_so_far)
        return res