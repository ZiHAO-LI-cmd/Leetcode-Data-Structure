class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        dp.insert(0, nums[0])
        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp.insert(i, dp[i - 1] + nums[i])
            else:
                dp.insert(i, nums[i])
        return max(dp)
