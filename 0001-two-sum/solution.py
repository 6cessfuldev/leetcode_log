class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ### Using Hash Map
        ### Time Complexity : O(n)
        ### Splace Complexity : O(n)
        num_map = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in num_map:
                return [num_map[compliment], i]
            num_map[num] = i


        ### Brute forces 
        ### Time Complexity : O(n(*n-1)/2) = O(n^2)
        ### Space Complexity : O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []
    
        
