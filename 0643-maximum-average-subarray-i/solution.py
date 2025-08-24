class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_avg = sum(nums[:k]) / k
        max_avg = window_avg

        for i in range(1, len(nums) -k+1):
            window_avg = window_avg - nums[i-1]/k + nums[i+k-1]/k
            max_avg = max(max_avg, window_avg)

        return max_avg

