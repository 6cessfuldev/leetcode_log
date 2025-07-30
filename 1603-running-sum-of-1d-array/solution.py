class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        psum = [nums[0]]

        for i in range(1, len(nums)):
            psum.append(nums[i] + psum[i-1])

        return psum
        
